import sys
import pytest

args = sys.argv

if args[1] == "all":
    pytest.main([])

elif args[1] == "get":
    pytest.main(["test_get_requests.py"])

elif args[1] == "post":
    pytest.main(["test_get_requests.py"])

elif args[1] == "put":
    pytest.main(["test_get_requests.py"])

elif args[1] == "patch":
    pytest.main(["test_get_requests.py"])

elif args[1] == "delete":
    pytest.main(["test_get_requests.py"])
