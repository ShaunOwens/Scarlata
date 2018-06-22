# Updates

6/21/2018
It turns out the file I downloaded yesterday is a fits file. It just has to have the extension converted. This is very very useful. First of all, now that I have access to downloading the files, I can start making the plan to loop through downloads and make cuts as I go. Second of all, for some unknown reason, my loop that matches dr8objid to MatchId is working now... I have not figured out why but I am not complaining. I now have a list stored to file of all of the matches between the Zoo catalog and the HSC catalog. This means I don't have to run the matching anymore, I can just move on to the plan for downloading. I will begin work on that today.

6/20/2018
I spent a lot of the day helping my roommate out. With the time I did have, I finished the paper I was reading, studied for the GWE, and tried to download a FITS file from the HSC catalog. I have a file that seems to have something in it. It is about 300MB but the file type is not something I have seen before. I am going to try and see if I can convert it in to something usable tomorrow.

6/19/2018
I got a message from Hugh about downloading data... It turns out there isn't documentation on downloading from the hsc catalog and he has is own set of code that does it. He sent me that so I could start figuring out what needs to happen in order to download the files. Spent a few hours studying for the GWE today. I have been keeping up with about 2 or so hours a day but I would like to step that up a little bit in the future.

6/18,2018
Start attempting to connect matches to images from the catalog. I have a number of matches using the ACS_F475W filter that I can test on to try and get just a couple images downloaded in the next few days. I am currently unable to find the pointer to the image file though. Tomorrow I will try a few other things I think might work to get the image downloaded. I will keep working with Clara from support to try and figure out my error.

6/12/2018-6/15/2018
Continue to try and match zoo catalog to HSC catalog. I have completed the requests on about half of the catalog but this can't continue. Repeating the request manually every 10-15 minutes just takes up too much of my time. I have started a conversation with the support staff of STSCI. This might help in the long run but righ now we are having a hard time replicating the error on both systems. Drove back to Minneapolis in this time. Meeting Thursday went well. I have to read my next paper more in depth next time.

6/11/2018
Use information obtained in meetings to start matching HSC sources to zoo sources. This involves using list comprehension to complete a query very quickly and save the results. This doesn't work exactly like I would like it to. It workes for one loop through a large query but breakes in the second one. It seems when calling the request again, the return result is the same as the last request no matter what is fed into the array assined to ra and dec. I have used several different sized lists, rerun the code printing every step to make sure it is doing what I want it to do, and even run the request outside of the loop and it is still broken. I will continue testing... It seems to be an error in the requesting and decoding of the data. I will try and tackle this tomorrow. Otherwise I can just run this in chunks of 3000-4000 over the course of a day or so and get the matching done.

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
