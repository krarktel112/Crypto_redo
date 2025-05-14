import shutil
import subprocess

def git_clone(repo_url, destination_path=None):
    """
    Clones a Git repository.

    Args:
        repo_url (str): The URL of the repository to clone.
        destination_path (str, optional): The local path where the repository should be cloned. 
                                         If None, the repository will be cloned to a directory 
                                         named after the repository in the current working directory.
    Raises:
        subprocess.CalledProcessError: If the git clone command fails.
    """
    command = ["git", "clone", repo_url]
    if destination_path:
        command.append(destination_path)
    try:
        subprocess.run(command, check=True, capture_output=True)
        print(f"Repository cloned successfully to {destination_path or repo_url.split('/')[-1]}")
    except subprocess.CalledProcessError as e:
         print(f"Error cloning repository: {e}")
         print(e.stderr.decode())

# Example usage:
shutil.rmtree("/data/data/com.termux/files/home/Crypto-track")
repo_url_to_clone = "https://github.com/krarktel112/Crypto-track.git"  # Replace with the actual repository URL
local_path_to_clone_to = "local_repo" # Optional: Specify a local directory
git_clone(repo_url_to_clone, local_path_to_clone_to)

