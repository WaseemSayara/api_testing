import sys
import pytest

args = sys.argv

print(args)
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
