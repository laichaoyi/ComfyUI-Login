**How to install ?** 

Open Terminal/cmd in ComfyUI/Custom_nodes \n
git clone https://github.com/laichaoyi/ComfyUI-Login.git
cd ComfyUI-Login
pip install -r requirements.txt

**How to use ?**

When ComfyUI starts up, the login panel will automatically appear. You can create an account or log in freely, and you can also change your password if needed.

If you are an admin and want to disable the account registration feature, open the password.py file inside the ComfyUI-Login folder, find **line 21**:
**ALLOW_REGISTER = True**, change it to **False**, then restart ComfyUI to disable account registration.

**Contact me: Facebook: https://www.facebook.com/ndle2**
