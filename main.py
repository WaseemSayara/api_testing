import sys
import pytest

args = sys.argv

print(args)

if len(args) > 1:
    if args[1] == "all":
        pytest.main([])

    elif args[1] == "get":
        print("entered get")
        pytest.main(["test_get_requests.py"])

    elif args[1] == "post":
        pytest.main(["test_post_requests.py"])

    elif args[1] == "put":
        pytest.main(["test_put_requests.py"])

    elif args[1] == "patch":
        pytest.main(["test_patch_requests.py"])

    elif args[1] == "delete":
        pytest.main(["test_delete_requests.py"])

    elif args[1] == "users":
        pytest.main(["-m users"])

    elif args[1] == "resource":
        pytest.main(["-m resource"])

    elif args[1] == "register":
        pytest.main(["-m register"])

    elif args[1] == "login":
        pytest.main(["-m login"])
