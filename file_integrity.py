import hashlib
import json
import os


BASELINE_FILE = "integrity_baseline.json"


def sha256_file(path):

    digest = hashlib.sha256()

    with open(path, "rb") as f:

        for block in iter(
            lambda: f.read(8192),
            b""
        ):

            digest.update(block)

    return digest.hexdigest()


def scan_folder(folder):

    data = {}

    for root, _, filenames in os.walk(folder):

        for name in filenames:

            path = os.path.join(
                root,
                name
            )

            if os.path.abspath(path) == os.path.abspath(
                BASELINE_FILE
            ):
                continue

            try:

                data[path] = sha256_file(path)

            except (PermissionError, OSError):

                pass

    return data


def create_baseline(folder):

    data = scan_folder(folder)

    with open(
        BASELINE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=2
        )

    return len(data)


def verify_baseline(folder):

    if not os.path.exists(BASELINE_FILE):

        return {
            "Status":
            "Baseline not found. Create one first."
        }

    with open(
        BASELINE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        old = json.load(f)

    current = scan_folder(folder)

    added = sorted(
        set(current) - set(old)
    )

    removed = sorted(
        set(old) - set(current)
    )

    changed = sorted(
        k for k in old.keys() & current.keys()
        if old[k] != current[k]
    )

    return {

        "Files checked": len(current),

        "Added": len(added),

        "Removed": len(removed),

        "Changed": len(changed),

        "Changed files": changed[:10],

        "Added files": added[:10],

        "Removed files": removed[:10]
    }