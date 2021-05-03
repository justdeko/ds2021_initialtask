import hashlib


def main(args):
    """
    Generates an md5-hash of a string which is combined by a passed parameter and my name.
    :param args:  dictionary with a course value for the key "course"
    :return: the hash in hex form
    """
    course = args.get("course", "Distributed Systems ")
    # generate hash with utf-8 encoding for spaces and such
    mhash = hashlib.md5(f"{course}Denis".encode("utf-8"))
    # print and return hash in hex format
    print(mhash.hexdigest())
    return {"the hash:": mhash.hexdigest()}
