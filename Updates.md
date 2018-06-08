# Updates

6/08/2018
Prepare for meeting.
Meeting went well. I now understand what I was doing wrong and what I need to do to fix it. Will start working on this tonight.
1. Use HSC matching to match sdss object to HSC object.
2. Select filters to use.
3. Query image that contain the objects interested in.
4. Filter out duplicate images.
5. Develope plan for downloading images and saving space on HDD.
6. Download images.
7. Make plan for cutting images.

6/07/2018
Study for GWE. ~1 hour.
Still working on code. Insufficient memory errors that must be figured out.
Prepare for meeting.

6/06/2018
Study for GWE. ~1 hour.
Work on code. Still not working.
Finish reading for the week. Write abstract.

6/05/2018
Complete code for loops. At least to my knowledge. The code can now loop through 800000 sources in 25 minutes but files are still empty. Tomorrow I will work with syntax more to try and figure out why it isn't downloading anything. Read some of the paper for this week.

6/04/2018
Start using new code to try and learn loops for downloading data. Unable to complete today but mostly reading documentation and understanding syntax.

6/01/2018
Study for GWE. ~1 hour.
Meeting.
Code works and I am able to download and cut all files but it will take almost a week to do one filer. This is too slow.
Learn about mass download from MAST API. Start learning code for that to be able to mass download.

5/31/2018: 
Study for GWE. ~2 hours.
Meeting.
Continue to try and understand where error is coming from. Data is not being processed properly. I don't understand why.
Finish update file for this week.
Talk with Hugh to try and fix my misunderstanding.
Hugh explained much. I didn't have an error at all it was just an empty vo table...
With this knowledge, I edited Hugh's code to be able to loop through many locations looking for vo tables. I was able to run the code with my computer off because its on a server. The loop I have run this time should be done by the meeting. At that time I can start searching for and downloading the fits files.

5/30/2018: 
Study for GWE. ~1 hour.
Start running code.
Imports: Easy. Understand.
Query: Few manipulations. Testing. Understand.
VO Table: Understand code but small problems. Code seems to work properly except for a datatype error that I can't seem to correct. Ask Hugh about it and bring it up at meeting.
Download: Fairly straightforward. Takes votable and downloads file from that location. Understand
Image: Figure manipulation. Understand.
Cutout: Need to understand.
Plot Cutout: Need to understand.

5/29/2018: 
Study for GWE. ~1 hour.
Read through code and begin learning sciserver.
Set up account in sciserver and beging learning query procedure.

5/28/2018: 
Read documentation and ask Hugh questions.

5/25/2018: 
Beging to understand how cuts work with the data obtained.
Research meeting. -Start sending these to Dr. Scarlata and Dr. Fortson. Continue learning how to use data. Transfer code to SciServer and begin using their resourses to complete tasks faster. Read all documentation  pertaining to what will be used.
Drive home...

5/24/2018: 
Study for the GWE. ~1 hour.
Download more vo files while waiting for meeting.
Ask questions about DS9.
Begin to learn how to cut image files down to correct specifications.
Prepare for meeting on Friday.

5/23/2018: 
Begin downloading image files. There are approximately 10 unique images in the first 140000 vo files. Another filter may be necessary.
Install and learn ds9.
Talk to John about what should be done next about the images. So far they look incorrect so changes must be made.
Study for the GWE. ~1 hour.
Spent a lot of the day driving.

5/22/2018: 
Begin studying for the gwe. ~2 hours.
Continue downloading vo files. At 138000 now.
Develope code to start downloading the fit image files from the vo files.
Choose device: WFC3 and filters: F475W, F475X.

5/21/2018: 
Continue to download VO files from hubble.
Through 114000 now. Will start to develope code to use vo files tomorrow.
Setup linux on personal computer for easier time with coding.
Begin organizing for studying for GWE. Will start tomorrow.

5/18/2018: 
Create script to download vo files for HST data.
Develope more code to try and get the loop to run through the shell script.
Run loop for some test itterations.
Scrap shell script and just use python...
It works.
Start downloading vo tables for all galaxies in the sdss survey.

5/17/2018: 
Download all fits for SDSS catalogues.
Begin understanding layout of fits to start matching to HST data as soon as possible.
Talk to John...
Start learning python to shell script.
http://docs.astropy.org/en/stable/io/fits/ - Fits information
http://docs.astropy.org/en/stable/io/votable/ - VO Table information
http://docs.astropy.org/en/stable/coordinates/matchsep.html - Matching for JH and NYU catalogues
http://hla.stsci.edu/hla_help.html#services - HST data
https://wwwmpa.mpa-garching.mpg.de/SDSS/DR7/SDSS_info.html - Ra_Dec Information

5/16/2018: 
Learn how to use GitHub. 
Create Update file for use by collaborators.
Read literature on catalogues in order to start using data tomorrow.
