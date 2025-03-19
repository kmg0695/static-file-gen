import os
import shutil


def recursive_copy(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for filename in os.listdir(source_dir):
        from_dir = os.path.join(source_dir, filename)
        to_dir = os.path.join(dest_dir, filename)
        print(f"Copying {from_dir} to {to_dir}...")
        if os.path.isfile(from_dir):
            shutil.copy(from_dir, to_dir)
        else:
            recursive_copy(from_dir, to_dir)
