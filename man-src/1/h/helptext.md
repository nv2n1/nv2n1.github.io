---
title: "helptext(1)"
name: "helptext"
section: "1"
letter: "h"
url: "/docs/linux/man/1-helptext/"
---

<h2>Geographic Resources Analysis Support System</h2>

 Commonly referred to as GRASS, this is a Geographic Information System (GIS) used for geospatial data management and analysis, image processing, graphics/map production, spatial modelling, and visualization. GRASS is currently used in academic and commercial settings around the world, as well as by many governmental agencies and environmental consulting companies.

<h2>Introduction</h2>

 GRASS data are stored in a directory referred to as DATABASE (also called &quot;GISDBASE&quot;). This directory has to be created with mkdir or a file manager, before starting to work with GRASS. Within this DATABASE, the projects are organized by project areas stored in subdirectories called LOCATIONs. 

 A LOCATION is defined by its coordinate system, map projection and geographical boundaries. The subdirectories and files defining a LOCATION are created automatically when GRASS is started the first time with a new LOCATION. 

 Each LOCATION can have many MAPSETs. Each MAPSET is a LOCATION's subdirectory. New MAPSET can be added at Grass startup. To remove a MAPSET, remove it's directory using your file manager or by rm -rf /path/to/the/mapset_to_delete. 

 One motivation to maintain different mapsets is to store maps related to project issues or subregions. Another motivation is to support simultaneous access of several users to the map layers stored within the same LOCATION, i.e. teams working on the same project. For teams a centralized GRASS DATABASE would be defined in a network file system (e.g. NFS). Besides access to his/her own MAPSET, each user can also read map layers in other users' MAPSETs, but s/he can modify or remove only the map layers in his/her own MAPSET. 

 You can learn more about mapsets and how to seamlessly access maps found in another MAPSET of the same LOCATION in the g.mapsets documentation. 

 When creating a new LOCATION, GRASS automatically creates a special MAPSET called PERMANENT where the core data for the project can be stored. Data in the PERMANENT MAPSET can only be added, modified or removed by the owner of the PERMANENT MAPSET; however, they can be accessed, analyzed, and copied into their own MAPSET by the other users. The PERMANENT MAPSET is useful for providing general spatial data (e.g. an elevation model), accessible but write-protected to all users who are working in the same LOCATION as the database owner. To manipulate or add data to PERMANENT, the owner would start GRASS and choose the relevant LOCATION and the PERMANENT MAPSET. This mapset also contains the DEFAULT_WIND file, which holds the default region boundary coordinate values for the location (which all users will inherit when they start using the database). Additionally, in all mapsets a WIND file is kept, for storing the current boundary coordinate values and the currently selected raster resolution. Users have the option of switching back to the default region at any time.

<h2>Creating a GRASS database</h2>

 To create the GRASS database: Find a place on your disk where you have write access and that has enough diskspace to hold your decompressed data. Create a subdirectory that will hold the general GRASS database (e.g. mkdir /data/GRASSDATA or mkdir /home/yourlogin/GRASSDATA). 

 

 Sample data such as the Spearfish sample dataset may be downloaded from <a rel="nofollow" HREF="http://grass.itc.it/download/data.php">http://grass.itc.it/download/data.php</a> and placed in the new database directory. 

 Click on the &quot;Create New Location&quot; button, which will take you to a text screen on which you can enter a new location name, and then continue by pressing &quot;ESC&quot;-&quot;RETURN&quot; - i.e. press (NOT hold) the ESC key, and then press the RETURN key on your keyboard. 

 Next you will need to assign parameters to the location such as the coordinate system and datum you want to use, the project area's boundary coordinates, and the default resolution for raster data:
<dl>
<dt>
<dd> Start by chosing between, X,Y, Latitude-Longitude, UTM, or dqother&quot; coordinate system. This choice depends on your data and the use you will make of it. You are then prompted for a single line of text describing the project area, for example &quot;Topo Map of the Alps&quot;.</dl>
 

 Next you are requested for some more information about the projection. Note that the prompts vary from projection to projection, an example follows:
<dl>
<dt>
<dd> (if you chose &quot;D - Other Projection&quot;) &quot;specify projection name&quot;: dqlist&quot; gives you the list of all available projections, examples are dqtmerc&quot; for Transverse Mercator, &quot;lcc&quot; for Lambert Conformal Conic, dqmoll&quot; for Mollweide, etc. specify datum name: again use &quot;list&quot; to get a list of available datums, examples are &quot;wgs84&quot;, &quot;nad27&quot;, &quot;eur79&quot;, etc. Enter Central Parallel: 0 if you want the Equator as the central parallel Enter Central Meridian: 0 if you want the Greenwich meridian as central meridian Enter Scale Factor at the Central Meridian Enter plural form of map units: for example, meters</dl>
 

 The next step is the description of the project area's boundary coordinates and the definition of the default raster resolution: 

 The default raster resolution (GRID RESOLUTION) has to be chosen according to your needs. Generally, it is advisable to work in steps of 0.25 (0.25, 0.5, 1.75, 2.00, 12.25 etc.). This resolution does not concern vector and site data since these are stored with their exact coordinate values. Note that every raster map may have its own resolution. You can leave this screen with &quot;ESC&quot;-&quot;RETURN&quot; and then if everything is correct accept the list of parameters that appears. 

 You will then be back to the startup screen to enter the mapset's name (if not already entered). Another &quot;ESC&quot;-&quot;RETURN&quot; will finally let you leave this screen. This mapset is created within the new location by answering &quot;yes&quot; to the next question. The mapset will use the parameters of the location (such as the region and resolution definitions) as its default parameters. 

 Now the project area, i.e. the location including a mapset, has been created. You have &quot;arrived&quot; in the GRASS system and can start working within this new location.

<h2>Further Reading</h2>

 Please have a look at the GRASS web site: <a rel="nofollow" HREF="http://grass.itc.it/gdp/index.php.">http://grass.itc.it/gdp/index.php.</a>

<h2>See also</h2>

 GRASS 6 launch manual page 
 GRASS 6 Reference Manual 

 <i>Last changed: $Date: 2007-05-30 10:26:52 +0200 (Wed, 30 May 2007) $</i> 

 Help Index 

<h2>Index</h2>


