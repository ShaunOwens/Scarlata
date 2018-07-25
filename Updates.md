# Updates

7/21-24/2018
In the past 3 weeks I have been studying for the GWE for about 2-3 hours per day. Starting tomorrow, I would like to move that to 3-4. I have started to impliment the methods discussed in the last update. Now that I have the accurate values, I am able to download accurate images. After muddling through my slow downloading process, I have confirmed that both the centering and the size for the petrosian radius both work for each image. I can now download and cutout accurate images of galaxies. My problem now is that sometimes by downloading code breakes. I had a meeting with Hugh again and we realized the code breaks because the file takes a few seconds to be bundled up in the download location the the mast server. My current code is tying to get the file there before it even exists. This is fixed by a try block of code and a while statement for another section. After some testing, this seems to fix my error. I can now download images and make cutouts for the correct locations and matches for each image at a single band. The remainder of the week will be deicated to creating a loop that downloads all images at one band and delets the larger images as it goes. This should be a much easier step.


7/18-20/2018
The cutouts are now centered. After many meetings with Hugh and lots of rewriting of code, the previous steps mentioned are now complete. The process was as follows. The first few days were spent making sure images could be downloaded properly. My first problem was that the location I was matching two was returning repeats. This means, although there were multiple galaxies per image, the images being downloaded were the same for each image. I was getting repeated images. This I was unable to fix before I realized why the galaxies were not being centered. The ra and dec values returned by the HSC catalog was only accurate to 4 decimal places in degrees which is not accurate enough. I was unable to determine why this was happening. Checking even further back, it seems the zoo2mainspecz values for ra and dec were also fairly inaccurate. In order to select more accurate ra and dec values but keep the "small" catalog, Hugh helped me select the objects that match the zoo catalog from the full sdss catalog. These matches have much more accurate values and also include the petrosian radius that I will need for the size of each image. Now that I have a table with all of this information and to much greater accuracy, I can hopefully get more accurate images.

7/12-17/2018
Most of the time for the past few days have been spent figuring out how to finish updating the rest of my code to the new versions. Now that the downloading is updated, the matching must be updated as well. This should be working now. As of this moment, I can download images a few at a time and make cutouts that are not necessarily centered or the correct size. These will be the focus of the next week or so.

7/9-11/2018
I will be showing back up on campus on Friday for a meeting at 2 if everyone will be there. This will be moved to monday. As for the past week, I have been working with Hugh a lot and I will try to stop taking too much of his time. The connection problems have been sorted out and I am once again able to download images. The services have been updated to a newer version on the MAST API so some of the outputs have changed and there are new errors in my code that I have to sort out. Part of this is waiting for the documentation to be updated on the MAST site so I can learn what the new formats are. Once I get this system figured out, it is back to making sure the images are centered. I noticed that the file that I am using to read in the information for the ra and dec seems to be truncating the size of the float value. This needs to be accurate up to 10^-7 degrees. The current accuracy is 10^-4. Once I can format images correctly again, I will begin sorting this error out. The files still contain one that is named System.String[]. The options I see are to either delete that file each time I download a set and make sure to include the deleted file in the next set, or save the name of the file associated with that file separately and rename it as it is being unpacked from the tar.gz file. The second option will most likely be more efficient. Once I have these problems figured out, I should be able to make just a few changes and finalize my downloading and cutting protocal to be able to download whatever we specify. Again I am still working on determining the radius but I would like to get the centering fixed first. As for the future. Once I have a code that will cut what we need, I want to determine which catalogs have classifications for morphology (just the zoo or some of the larger catalogs). This will speed up the process of matching between the two galaxy zoo classifications (morphology from sdss and morphology from hst). Then I can determine the size of the data set we have and determine what is necessary for the next steps.

7/3-6/2018
So far, the work on centering the images has been slow going. I have the files converted to another type to see if that will prevent the truncation of the floats. The problem now is I belive the MAST service is down. I am unable to complete a query due to a connection error. I will give it through the weekend to see if it is back up then I will contact support again to see if something is wrong. Meanwhile, I have been studying for a few hours a day. I will contact Dr. Fortson this weekend to ask when to be back to campus for our next meeting. I will also read a paper this weekend.

7/2/2018
After the meeting today I have a few things I need to make sure to understand. The following is a list, to my knowledge, of what the goals of this project are.
Have the ability to produce many images from the HST that match to images obtainable via the SDSS.
These images, if there are enough of them and if it is deemed necessary, can be used to start a galaxy zoo project.
This project will consist of classifications of morphology which will then be associated with the mass of the galazy chosen.
This information will be used to crossreference a paper which claims that there is a morphology change of galaxies at a certain mass.
This transition if 10^9.5-10^10.5 times the mass of the sun.
Lower than this range, galaxies from in disorganized ways.
In this range, galaxies form in a disk shape.
Above this range, galaxies from in a spheroidal shape.
Beyond this, I am unsure where the project will go next.

6/22-30/2018
Over the past week I have continued developing code to be able to run the downloading procedure on any catalog we would like to match to. This included running the original matching loop and saving the data to an astropy table. This comes in about 400 separate tables that I spent a day (with the help of Michael) figuring out how to put together into one table and save it to file so I won't have to run it again. With this done I started developing code to take the match IDs and create a list of images associated with those match IDs. There will be some repeats in this procedure. This means I had to go back through and create a dictionary where the key is the name of the image and the information in the dictionary is the actual match IDs associated with that image. This will allow me to only download each image once instead of multiple times for the repeating matches. Once this was working, I developed some code to start downloading batches of images in groups of 4 for testing. My code now downloads the images, selects the location of the matches on the image, cuts them out, and saves this information to a new fits file. There are a few things I still need to iron out though. The radius is still not correct for each cut, the cuts themselves are not perfectly centered, the downloading process still spits out a System.String[] file which I cannot use for cuts easily, and I still need to get it to loop through the entire dictionary. These will be my steps going forward.

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
