import hashlib


def main(args):
    course = args.get("course", "Distributed Systems ")
    mhash = hashlib.md5(f"{course}Denis".encode("utf-8"))
    print(mhash.hexdigest())
    return {"the hash:": mhash.hexdigest()}
