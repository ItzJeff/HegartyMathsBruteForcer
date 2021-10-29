iscoolguy#3341 https://www.youtube.com/channel/UCAskB2OCC944KGgQ9fr64EA
This is a brute force tool that is used to brute force most websites

Requirements
pip2 install selenium
pip2 install requests
Chromium and chromedriver are required

You can download chromedriver here: http://chromedriver.chromium.org/downloads for this fork or through https://mega.nz/file/iNlmhBIC#qc1ltLAYYE1h3jjYA3fp6dShLuGeDQmHuOzdc5bj544, create a folder in your C drive called 'webdrivers' and place the executable file inside. 


Installation instructions:
Step1, copy Python27 folder to > This PC > Local Disk (C:)
Step2, copy chromedriver_win32.zip to > This PC > Local Disk (C:) #do not extract
Step3, open terminal and type in manually: "cd /Python27", "pip2 install selenium", "pip2 install requests" #wait until fully installed, please.
Step4, open File explorer and go to > This PC > Local Disk (C:) > Python27 
Step5, scroll and find "main.py", select & right-click, select option "Edit with IDLE"
Step6, scroll to variables: school, username1-5 and edit it towards your victim #self explanatory, keep quotation marks around names, birthdate. 
Step7, download the "Win_x64_902222_mini_installer” and run #it will NOT work if you already have Chrome installed
Step7.1, a temporary file called "CR_#####.tmp" will be created, hastily open it, double click application: "setup" to run.
Step7.2, launch Task Manager service via start menu (Windows Key + "Task Manager" + ENTER)
Step7.3, sort highest of Disk usage and you'll find "Chromium installer", wait for chromium to completely install.
Step7.4, launch Program and Features service via Window run (Windows Key + R + wait + "appwiz.cpl" + ENTER)
Step7.5, find Google Chrome, select & right-click, select option "Uninstall" #make sure to close the all Chrome instances before selecting "Uninstall".
Step7.6, launch Chromium application via start menu (Windows Key + "Chromium" + ENTER)
Step8, open terminal and type in manually: "cd /Python27", "python2 main.py" #WARNING: 8 chrome tabs will pop up, do not go back to the terminal and start clicking around there, if everything stops, press Ctrl +C once. (ONLY ONCE)
Step9, wait/leave to run overnight, make sure your PC doesn't automatically go to sleep otherwise tabs and resources will be paralysed.
Step10, when you want to use another wordlist:
Step10.1, open File explorer and go to > This PC > Local Disk (C:) > Python27 
Step10.2, scroll and find "main.py", select & right-click, select option "Edit with IDLE"
Step10.3, scroll to variable: "openagain" replace "wordlist3.txt" with another such as "wordlist4.txt"
 
Notes:
If you see alot of "failed element not found"s then the program is being put into virtual memory therefore leading to the attempt being skipped, 
to mitigate this regularly un-minimise the chrome tabs to refresh primary memory, then press the "Login" button to resume.
The provided wordlists consists of @(NOUN)%%%, where @(NOUN) represents a random noun concatenated with a random combination of numbers, referred to as %%%. Each noun is repeated 1000times to satisfy 000-999, therefore it is not certain that all passwords are on these included wordlists. If you have your own wordlist you'd like to try yourself, then move it to C:/Python27/ directory and edit the script shown in Steps 10-10.3.
It is recommended to check for efficiency & accuracy updates by your distributor.
 
All vulnerabilities should be abused before they're patched. You do you.
