"""Offline portfolio-only contract excerpt, not the private instrument schema."""
import json, math

def summarize_patch(patch):
    cutoff, release = patch["cutoff_hz"], patch["release_seconds"]
    if any(type(v) not in (int, float) or not math.isfinite(v) for v in (cutoff, release)):
        raise ValueError("Finite numeric values required")
    if not 20 <= cutoff <= 20000 or not 0.01 <= release <= 20:
        raise ValueError("Example range exceeded")
    return {"synthetic": True, "cutoff_hz": cutoff, "release_seconds": release,
            "status": "interface_only_no_audio_rendering"}

if __name__ == "__main__":
    print(json.dumps(summarize_patch({"cutoff_hz": 1800, "release_seconds": 2.0}), indent=2))
