import git
import shutil
import pytest
import os

repo = git.Repo('/Users/omkarsalpekar/Documents/Research/RISELab/modin')
sha = repo.head.object.hexsha
print(sha)

# repo.git.checkout('HEAD~1')
# sha = repo.head.object.hexsha
# print(sha)
# print(type(sha))

FINAL_HASH = "cccea0bed17349727ba13376ee7cc62ac5619852"
# TEMP_FINAL_HASH = "5e82c60516bc310a631e6e2f00c02ecd8af33049"
# TEMP_FINAL_HASH = "e071b337e6162422d9d64e5c9a865cd3ae1f65cc" # only runs for one commit
TEMP_FINAL_HASH = "0302c95c91a4178e82edfa8e2fb169a2402fb1b6"
# START_HASH = ""

# repo.git.checkout(START_HASH)

while repo.head.object.hexsha != TEMP_FINAL_HASH:
    print(repo.head.object.hexsha)
    # copy test script into the modin repo
    shutil.copy("../test_modin.py", "./modin/pandas/test/")
    # run tests and get results
    pytest.main(["modin/pandas/test/test_modin.py", "--benchmark-autosave"])
    # add to json file
    # shutil.copy(".benchmarks/*", "../modin_benchmarks/")
    # delete the test script file
    os.remove("./modin/pandas/test/test_modin.py")
    # checkout previous commit
    repo.git.checkout('HEAD~1')

# master branch stuff
# master_hash = "cccea0bed17349727ba13376ee7cc62ac5619852"
repo.git.checkout("master")
shutil.copy("../test_modin.py", "./modin/pandas/test/")
pytest.main(["modin/pandas/test/test_modin.py", "--benchmark-autosave"])
os.remove("./modin/pandas/test/test_modin.py")


#then manually move everything from /.benchmarks to someplace else
#checkout to prof branch
