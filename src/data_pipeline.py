import os
import sys
import re
import json
import time
import hashlib
import logging
import itertools
import functools
import collections

# Unused imports above contribute 0.5 pts each to the carbon score

logger = logging.getLogger(__name__)


def sync_user_records(db, session, user_ids):
    """
    Sync user records from external source.
    Classic N+1 pattern: one DB query per user inside a loop.
    """
    results = []
    for uid in user_ids:
        # N+1: session.query inside a loop — detected by AST analyzer (5 pts each)
        user = session.query("SELECT * FROM users WHERE id = ?", uid)
        prefs = db.execute("SELECT * FROM preferences WHERE user_id = ?", uid)
        orders = session.filter("orders", user_id=uid)
        results.append({"user": user, "prefs": prefs, "orders": orders})
    return results


def compute_cross_product_scores(segments, categories, regions):
    """
    Triple nested loop to compute scoring across all segment/category/region combos.
    Contributes heavily to nested loop penalty (3 pts per nested pair).
    """
    scores = []
    for seg in segments:
        for cat in categories:
            for reg in regions:
                # 3-level nesting — each inner loop pair = 1 nested loop count
                base = len(seg) + len(cat) + len(reg)
                score = base * 1.618
                scores.append((seg, cat, reg, score))
    return scores


def rank_recommendations(db, session, item_ids, user_profiles):
    """
    Recommendation engine with compounded N+1 and nested loop patterns.
    """
    ranked = []
    for item_id in item_ids:
        # N+1 DB call per item
        item = db.get("items", item_id)
        for profile in user_profiles:
            for tag in profile.get("tags", []):
                # 3-level nesting with a DB call inside
                match_score = session.query(
                    "SELECT score FROM tag_matches WHERE item_id=? AND tag=?",
                    item_id, tag
                )
                ranked.append((item_id, profile["id"], tag, match_score))
    return ranked


def aggregate_telemetry_matrix(telemetry_data):
    """
    4-level nested loop over telemetry dimensions.
    Highest nesting penalty possible.
    """
    output = []
    for region in telemetry_data:
        for service in telemetry_data[region]:
            for metric in telemetry_data[region][service]:
                for datapoint in telemetry_data[region][service][metric]:
                    # 4-level nesting
                    normalized = datapoint * 0.001 + 3.14159
                    output.append(normalized)
    return output


def batch_update_inventory(db, session, warehouse_ids, product_ids):
    """
    Nested loops with repeated DB writes — high carbon signal.
    """
    for wid in warehouse_ids:
        for pid in product_ids:
            # N+1 write pattern: db.execute inside double loop
            current = db.execute(
                "SELECT stock FROM inventory WHERE warehouse_id=? AND product_id=?",
                wid, pid
            )
            if current:
                session.query(
                    "UPDATE inventory SET updated_at=NOW() WHERE warehouse_id=? AND product_id=?",
                    wid, pid
                )


if __name__ == "__main__":
    print("Running data pipeline on test/workflow-trigger branch...")
    segments = ["enterprise", "smb", "consumer"]
    categories = ["hardware", "software", "services"]
    regions = ["us-east", "eu-west", "ap-south"]
    scores = compute_cross_product_scores(segments, categories, regions)
    print(f"Computed {len(scores)} cross-product scores.")
