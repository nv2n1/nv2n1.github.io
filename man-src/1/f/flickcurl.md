---
title: "flickcurl(1)"
name: "flickcurl"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flickcurl/"
description: "flickcurl – call Flickr API"
---

<h2>NAME</h2>
<p> flickcurl &#8211; call Flickr API</p>
<h2>SYNOPSIS</h2>
<p> <code>flickcurl</code> <code>-a </code><i>FROB</i><br />
 <code>flickcurl</code> [<code>-d </code><i>DELAY</i>] [<code>-h</code>] [<code>-o FILE</code>] [<code>-q</code>] [<code>-v</code>] [<code>-V</code>] [<i>commands</i>] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>flickcurl</code> is a utility program to call the Flickr APIs via the flickcurl library. Run <i>flickcurl -h</i> to get a list of the supported commands and their arguments. </p>
<p> The program requires configuring before use to work with the Flickr APIs. Run <code>flickcurl</code> without any options to get the instructions for registering the application and creating the initial configuration file <i>~/.flickcurl.conf</i> from the registration information.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-a </code><i>FROB</i>, &#8211;auth <i>FROB</i></p>
<dd> Authenticate with a <i>FROB</i> and update the authentication file. The program will exit after updating the file.</p>
<dt><code>-d </code><i>DELAY</i>, &#8211;delay <i>DELAY</i></p>
<dd> Set delay between requests to <i>DELAY</i> milliseconds.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options and exit.</p>
<dt><code>-o </code><i>FILE</i>, &#8211;output <i>FILE</i></p>
<dd> Write the results of format feed API calls to <i>FILE</i></p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Display less information while the program runs.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display the version of the program and exit.</p>
<dt><code>-V, &#8211;verbose</code></p>
<dd> Display more information while the program runs.</dl>
<h2>COMMANDS</h2>
<p> In the following list of commands:<br />
 <i>PER-PAGE</i> is photos per result page or &#8216;-&#8216; for default (10)<br />
 <i>PAGE</i> is result page number or &#8216;-&#8216; for default (1 = first page) </p>
<dl>
<dt><code>activity.userComments</code> <i>[PER-PAGE [PAGE]]</i></p>
<dd> Get photos commented on by the caller.</p>
<dt><code>activity.userPhotos</code> <i>[TIMEFRAME [PER-PAGE [PAGE]]]</i></p>
<dd> Get recent activity on the caller&#8217;s photos.</p>
<dt><code>auth.checkToken</code> <i>TOKEN</i></p>
<dd> Get the credentials attached to an authentication TOKEN.</p>
<dt><code>auth.getFrob</code> <i></i></p>
<dd> Get a frob to be used during authentication.</p>
<dt><code>auth.getFullToken</code> <i>MINI-TOKEN</i></p>
<dd> Get the full authentication token for MINI-TOKEN.</p>
<dt><code>auth.getToken</code> <i>TOKEN</i></p>
<dd> Get the auth token for the FROB, if one has been attached.</p>
<dt><code>blogs.getList</code> <i></i></p>
<dd> Get a list of configured blogs for the calling user.</p>
<dt><code>blogs.getServices</code> <i></i></p>
<dd> Get a list of blog services.</p>
<dt><code>blogs.postPhoto</code> <i>BLOG-ID PHOTO-ID TITLE DESCRIPTION [BLOG-PASSWORD]</i></p>
<dd> Post PHOTO-ID to blog BLOG-ID with TITLE, DESCRIPTION and optional password.</p>
<dt><code>collections.getInfo</code> <i>COLLECTION-ID</i></p>
<dd> Get information on collection COLLECTION-ID</p>
<dt><code>collections.getTree</code> <i>[COLLECTION-ID|- [USER-ID|-]]</i></p>
<dd> Get tree of collections COLLECTION-ID for USER-ID</p>
<dt><code>commons.getInstitutions</code> <i></i></p>
<dd> Get list of institutions</p>
<dt><code>contacts.getList</code> <i>[FILTER [PAGE [PER-PAGE]]]</i></p>
<dd> Get a list of contacts with optional FILTER</p>
<dt><code>contacts.getListRecentlyUploaded</code> <i>[DATE-LAST-UPLOAD [FILTER]]</i></p>
<dd> Get a list of recent uploading contacts since DATE-LAST-UPLOAD with optional FILTER</p>
<dt><code>contacts.getPublicList</code> <i>USER-NSID [PAGE [PER-PAGE]]</i></p>
<dd> Get the contact list for user USER-NSID</p>
<dt><code>contacts.getTaggingSuggestions</code> <i>[PAGE [PER-PAGE [INCLUDE-SELF [INCLUDE-ADDRESS-BOOK]]]]</i></p>
<dd> Get tagging suggestions</p>
<dt><code>favorites.add</code> <i>PHOTO-ID</i></p>
<dd> Adds PHOTO-ID to the current user&#8217;s favorites.</p>
<dt><code>favorites.getContext</code> <i>PHOTO-ID USER-NSID [NUM-PREV [NUM-NEXT [EXTRAS]]]</i></p>
<dd> Get context photos around USER-ID&#8217;s favorite PHOTO-ID.</p>
<dt><code>favorites.getList</code> <i>USER-NSID [PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get a list of USER-NSID&#8217;s favorite photos.</p>
<dt><code>favorites.getPublicList</code> <i>USER-NSID [PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get a list of USER-NSID&#8217;s favorite public photos.</p>
<dt><code>favorites.remove</code> <i>PHOTO-ID</i></p>
<dd> Removes PHOTO-ID to the current user&#8217;s favorites.</p>
<dt><code>galleries.addPhoto</code> <i>GALLERY-ID PHOTO-ID TEXT</i></p>
<dd> Add photo PHOTO-ID to galleries GALLERY-ID with TEXT</p>
<dt><code>galleries.create</code> <i>TITLE [DESCRIPTION [PRIMARY-PHOTO-ID]</i></p>
<dd> Create a new gallery with TITLE, DESCRIPTION and PRIMARY-PHOTO_ID.</p>
<dt><code>galleries.editMeta</code> <i>GALLERY-ID TITLE [DESCRIPTION]</i></p>
<dd> Set the TITLE and/or DESCRIPTION of a GALLERY-ID.</p>
<dt><code>galleries.editPhoto</code> <i>GALLERY-ID PHOTO-ID COMMENT</i></p>
<dd> Set the COMMENT for PHOTO-ID in GALLERY-ID.</p>
<dt><code>galleries.editPhotos</code> <i>GALLERY-ID PRIMARY-PHOTO-ID PHOTO-IDS,&#8230;</i></p>
<dd> Set the PHOTO-IDs of a GALLERY-ID and PRIMARY-PHOTO-ID.</p>
<dt><code>galleries.getInfo</code> <i>GALLERY-ID</i></p>
<dd> Get information about GALLERY-ID.</p>
<dt><code>galleries.getList</code> <i>USER-ID [PER-PAGE [PAGE]]</i></p>
<dd> Get list of galleries for a USER-ID with optional paging</p>
<dt><code>galleries.getListForPhoto</code> <i>PHOTO-ID [PER-PAGE [PAGE]]</i></p>
<dd> Get list of galleries PHOTO-ID appears in with optional paging</p>
<dt><code>galleries.getPhotos</code> <i>GALLERY-ID [EXTRAS [PER-PAGE [PAGE [FORMAT]]]]</i></p>
<dd> Get the list of photos in GALLERY-ID with options.</p>
<dt><code>getphotoid</code> <i>IMAGE-URL</i></p>
<dd> Get the photo id from a raw flickr farm IMAGE-URL</p>
<dt><code>groups.browse</code> <i>[CAT-ID]</i></p>
<dd> Browse groups below category CAT-ID (or root).</p>
<dt><code>groups.getInfo</code> <i>GROUP-ID [LANG]</i></p>
<dd> Get information on group GROUP-ID with language LANG.</p>
<dt><code>groups.join</code> <i>GROUP-ID [ACCEPT-RULES]</i></p>
<dd> Join a group GROUP-ID with optional accepting of rules.</p>
<dt><code>groups.joinRequest</code> <i>GROUP-ID MESSAGE ACCEPT-RULES</i></p>
<dd> Request to join a group GROUP-ID using MESSAGE and accept rules.</p>
<dt><code>groups.leave</code> <i>GROUP-ID [DELETE-PHOTOS]</i></p>
<dd> Leave a group GROUP-ID and optionally delete photos.</p>
<dt><code>groups.members.getList</code> <i>GROUP-ID [MEMBER-TYPES [PER-PAGE [PAGE]]]</i></p>
<dd> Get list of MEMBER-TYPES types members of group GROUP-ID.</p>
<dt><code>groups.pools.add</code> <i>PHOTO-ID GROUP-ID</i></p>
<dd> Add PHOTO-ID in GROUP-ID pool.</p>
<dt><code>groups.pools.getContext</code> <i>PHOTO-ID GROUP-ID</i></p>
<dd> Get next and previous photos for PHOTO-ID in GROUP-ID pool.</p>
<dt><code>groups.pools.getGroups</code> <i>[PER-PAGE [PAGE]]</i></p>
<dd> Get list of groups a user can add to.</p>
<dt><code>groups.pools.getPhotos</code> <i>GROUP-ID [PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get list of photos in GROUP-ID.</p>
<dt><code>groups.pools.remove</code> <i>PHOTO-ID GROUP-ID</i></p>
<dd> Remove PHOTO-ID from group GROUP-ID.</p>
<dt><code>groups.search</code> <i>TEXT [PER-PAGE [PAGE]]</i></p>
<dd> Search for groups matching TEXT paging PER-PAGE and PAGE.</p>
<dt><code>interestingness.getList</code> <i>[PARAMS]</i></p>
<dd> Get interesting photos with optional parameters<br />
 date DATE<br />
 extras EXTRAS<br />
 per-page PER-PAGE<br />
 page PAGE<br />
 format FORMAT</p>
<dt><code>machinetags.getNamespaces</code> <i>[PREDICATE [PER-PAGE [PAGE]]]</i></p>
<dd> Get a list of namespaces with optional PREDICATE</p>
<dt><code>machinetags.getPairs</code> <i>[NAMESPACE [PREDICATE [PER-PAGE [PAGE]]]]</i></p>
<dd> Get a list of unique NAMESPACE and PREDICATE pairs</p>
<dt><code>machinetags.getPredicates</code> <i>[NAMESPACE [PER-PAGE [PAGE]]]</i></p>
<dd> Get a list of unique predicates optionally by NAMESPACE</p>
<dt><code>machinetags.getRecentValues</code> <i>[NAMESPACE|- [PREDICATE|- [ADDED-SINCE]]]</i></p>
<dd> Get a list of recent machinetags for NAMESPACE and PREDICATE since ADDED-SINCE</p>
<dt><code>machinetags.getValues</code> <i>NAMESPACE PREDICATE [PER-PAGE [PAGE]]</i></p>
<dd> Get a list of unique values for a NAMESPACE and PREDICATE</p>
<dt><code>oauth.create</code> <i>[CALLBACK]</i></p>
<dd> Create OAuth request token/secret pair and show the authentication URL</p>
<dt><code>oauth.upgrade</code> <i></i></p>
<dd> Upgrade legacy authentication to OAuth</p>
<dt><code>oauth.verify</code> <i>REQUEST-TOKEN REQUEST-TOKEN-SECRET VERIFIER</i></p>
<dd> Verify an OAuth request from `oauth.create&#8217;</p>
<dt><code>panda.getList</code> <i></i></p>
<dd> get the current list of pandas</p>
<dt><code>panda.getPhotos</code> <i>PANDA</i></p>
<dd> ask a PANDA for a list of recent public and safe photos</p>
<dt><code>people.findByEmail</code> <i>EMAIL</i></p>
<dd> get a user&#8217;s NSID from their EMAIL address</p>
<dt><code>people.findByUsername</code> <i>USERNAME</i></p>
<dd> get a user&#8217;s NSID from their USERNAME</p>
<dt><code>people.getGroups</code> <i>USER-ID [GROUP-EXTRAS]</i></p>
<dd> Get list of groups USER-ID is a member of</p>
<dt><code>people.getInfo</code> <i>USER-NSID</i></p>
<dd> Get information about one person with id USER-NSID</p>
<dt><code>people.getPhotos</code> <i>USER-NSID</i></p>
<dd> Get photos from user USER-NSID with optional parameters<br />
 safe-search 1-3<br />
 min-upload-date DATE<br />
 max-upload-date DATE<br />
 min-taken date DATE<br />
 max-taken-date DATE<br />
 content-type 1-7<br />
 privacy-filter 1-5<br />
 per-page PER-PAGE<br />
 page PAGE<br />
 format FORMAT</p>
<dt><code>people.getPhotosOf</code> <i>USER-NSID [PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get public photos of a user USER-NSID</p>
<dt><code>people.getPublicGroups</code> <i>USER-NSID</i></p>
<dd> Get list of public groups a user is a member of</p>
<dt><code>people.getPublicPhotos</code> <i>USER-NSID [PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get public photos for a user USER-NSID</p>
<dt><code>people.getUploadStatus</code> <i></i></p>
<dd> Get calling user upload status</p>
<dt><code>photos.addTags</code> <i>PHOTO-ID TAGS</i></p>
<dd> Add TAGS to a PHOTO-ID.</p>
<dt><code>photos.comments.addComment</code> <i>PHOTO-ID TEXT</i></p>
<dd> Add a photo comment TEXT to PHOTO-ID.</p>
<dt><code>photos.comments.deleteComment</code> <i>COMMENT-ID</i></p>
<dd> Delete a photo comment COMMENT-ID.</p>
<dt><code>photos.comments.editComment</code> <i>COMMENT-ID TEXT</i></p>
<dd> Edit a photo comment COMMENT-ID to have new TEXT.</p>
<dt><code>photos.comments.getList</code> <i>PHOTO-ID</i></p>
<dd> Get the comments for a photo PHOTO-ID.</p>
<dt><code>photos.comments.getRecentForContacts</code> <i>[PARAMS]</i></p>
<dd> Get the list of photos for user contacts with recent comments<br />
 since DATE-LAST-COMMENT filter CONTACTS-FILTER<br />
 per-page PER-PAGE page PAGE format FORMAT</p>
<dt><code>photos.delete</code> <i>PHOTO-ID</i></p>
<dd> Delete a PHOTO-ID.</p>
<dt><code>photos.geo.getLocation</code> <i>PHOTO-ID</i></p>
<dd> Get the geo location for a photo PHOTO-ID.</p>
<dt><code>photos.geo.getPerms</code> <i>PHOTO-ID</i></p>
<dd> Get the geo perms for a photo PHOTO-ID.</p>
<dt><code>photos.geo.removeLocation</code> <i>PHOTO-ID</i></p>
<dd> Remove the location for a photo PHOTO-ID.</p>
<dt><code>photos.geo.setLocation</code> <i>PHOTO-ID LAT LONG ACCURACY</i></p>
<dd> Set the location for a photo PHOTO-ID.</p>
<dt><code>photos.geo.setPerms</code> <i>PHOTO-ID IS-PUBLIC IS-CONTACT IS-FRIEND IS-FAMILY</i></p>
<dd> Set the geo perms for a photo PHOTO-ID.</p>
<dt><code>photos.getAllContexts</code> <i>PHOTO-ID</i></p>
<dd> Get all visible sets and pools the PHOTO-ID belongs to.</p>
<dt><code>photos.getContactsPhotos</code> <i></i></p>
<dd> Get a list of recent photos from the calling users&#8217; contacts</p>
<dt><code>photos.getContactsPublicPhotos</code> <i>USER-NSID [FORMAT]</i></p>
<dd> Get a list of recent public photos from USER-NSID&#8217;s contacts</p>
<dt><code>photos.getContext</code> <i>PHOTO-ID</i></p>
<dd> Get next and previous photos for a PHOTO-ID in a photostream.</p>
<dt><code>photos.getCounts</code> <i>DATES TAKEN-DATES</i></p>
<dd> Get the counts for a set of DATES or TAKEN-DATES.</p>
<dt><code>photos.getExif</code> <i>PHOTO-ID</i></p>
<dd> Get EXIF information about one photo with id PHOTO-ID</p>
<dt><code>photos.getFavorites</code> <i>PHOTO-ID [PER-PAGE [PAGE]]</i></p>
<dd> Get favourites information about one photo with id PHOTO-ID</p>
<dt><code>photos.getInfo</code> <i>PHOTO-ID [SECRET]</i></p>
<dd> Get information about one photo PHOTO-ID with optional SECRET</p>
<dt><code>photos.getNotInSet</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get list of photos that are not in any set</p>
<dt><code>photos.getPerms</code> <i>PHOTO-ID</i></p>
<dd> Get a photo viewing and commenting permissions</p>
<dt><code>photos.getRecent</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get list of recent photos</p>
<dt><code>photos.getSizes</code> <i>PHOTO-ID</i></p>
<dd> Get sizes of a PHOTO-ID</p>
<dt><code>photos.getUntagged</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get list of photos that are not tagged</p>
<dt><code>photos.getWithGeoData</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get list of photos that have geo data</p>
<dt><code>photos.getWithoutGeoData</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get list of photos that do not have geo data</p>
<dt><code>photos.licenses.getInfo</code> <i></i></p>
<dd> Get list of available photo licenses</p>
<dt><code>photos.licenses.setLicense</code> <i>PHOTO-ID LICENSE-ID</i></p>
<dd> Get photo PHOTO-ID license to LICENSE-ID</p>
<dt><code>photos.notes.add</code> <i>PHOTO-ID X Y W H TEXT</i></p>
<dd> Add a note (X, Y, W, H, TEXT) to a photo with id PHOTO-ID</p>
<dt><code>photos.notes.delete</code> <i>NOTE-ID</i></p>
<dd> Delete a note with id NOTE-ID</p>
<dt><code>photos.notes.edit</code> <i>NOTE-ID X Y W H TEXT</i></p>
<dd> Edit note NOTE-ID to (X, Y, W, H, TEXT)</p>
<dt><code>photos.people.add</code> <i>PHOTO-ID USER-ID X Y W H</i></p>
<dd> Mark USER-ID appearing in PHOTO-ID at (X, Y, W, H)</p>
<dt><code>photos.people.delete</code> <i>PHOTO-ID USER-ID</i></p>
<dd> Mark USER-ID as not appearing in PHOTO-ID</p>
<dt><code>photos.people.deleteCoords</code> <i>PHOTO-ID USER-ID</i></p>
<dd> Mark USER-ID as not appearing at coordinates in PHOTO-ID</p>
<dt><code>photos.people.editCoords</code> <i>PHOTO-ID USER-ID X Y W H</i></p>
<dd> Update USER-ID appearing in PHOTO-ID to coords (X, Y, W, H)</p>
<dt><code>photos.people.getList</code> <i>PHOTO-ID</i></p>
<dd> Get list of users appearing in PHOTO-ID</p>
<dt><code>photos.recentlyUpdated</code> <i>MIN-DATE [PER-PAGE [PAGE [FORMAT]]]</i></p>
<dd> Get list of photos that were recently updated</p>
<dt><code>photos.removeTag</code> <i>PHOTO-ID TAG-ID</i></p>
<dd> Remove a tag TAG-ID from a photo.</p>
<dt><code>photos.search</code> <i>[PARAMS] tags TAGS&#8230;</i></p>
<dd> Search for photos/videos with many optional parameters<br />
 user USER<br />
 tag-mode any|all<br />
 text TEXT<br />
 (min|max)-(upload|taken)-date DATE<br />
 license LICENSE<br />
 privacy PRIVACY<br />
 bbox a,b,c,d<br />
 sort date-(posted|taken)-(asc|desc)|interestingness-(desc|asc)|relevance<br />
 accuracy 1-16<br />
 safe-search 1-3<br />
 type 1-4<br />
 machine-tags TAGS<br />
 machine-tag-mode any|all<br />
 group-id ID<br />
 place-id ID<br />
 extras EXTRAS<br />
 per-page PER-PAGE<br />
 page PAGES<br />
 media all|photos|videos<br />
 has-geo<br />
 lat LAT lon LON radius RADIUS radius-units km|mi<br />
 contacts (all|ff)<br />
 format FORMAT<br />
 woeid WOEID<br />
 geo-context 1-2<br />
 in-commons<br />
 in-gallery</p>
<dt><code>photos.setContentType</code> <i>PHOTO-ID TYPE</i></p>
<dd> Set photo TYPE to one of &#8216;photo&#8217;, &#8216;screenshot&#8217; or &#8216;other&#8217;</p>
<dt><code>photos.setDates</code> <i>PHOTO-ID POSTED TAKEN GRANULARITY</i></p>
<dd> Set a photo POSTED date, TAKEN date with GRANULARITY</p>
<dt><code>photos.setMeta</code> <i>PHOTO-ID TITLE DESCRIPTION</i></p>
<dd> Set a photo TITLE and DESCRIPTION</p>
<dt><code>photos.setPerms</code> <i>PHOTO-ID IS-PUBLIC IS-FRIEND IS-FAMILY PERM-COMMENT PERM-ADDMETA</i></p>
<dd> Set a photo viewing and commenting permissions</p>
<dt><code>photos.setSafetyLevel</code> <i>PHOTO-ID SAFETY-LEVEL HIDDEN</i></p>
<dd> Set a photo&#8217;s SAFETY-LEVEL and HIDDEN flag</p>
<dt><code>photos.setTags</code> <i>PHOTO-ID TAGS</i></p>
<dd> Set the tags for a PHOTO-ID to TAGS.</p>
<dt><code>photos.transform.rotate</code> <i>PHOTO-ID DEGREES</i></p>
<dd> Rotate PHOTO-ID by 90/180/270 DEGREES</p>
<dt><code>photos.upload.checkTickets</code> <i>TICKET-IDS&#8230;</i></p>
<dd> Get the status of upload TICKET-IDS</p>
<dt><code>photosets.addPhoto</code> <i>PHOTOSET-ID PHOTO-ID</i></p>
<dd> Add PHOTO-ID to a PHOTOSET-ID.</p>
<dt><code>photosets.comments.addComment</code> <i>PHOTOSET-ID TEXT</i></p>
<dd> Add a comment TEXT to photoset PHOTOSET-ID.</p>
<dt><code>photosets.comments.deleteComment</code> <i>COMMENT-ID</i></p>
<dd> Delete a photoset comment COMMENT-ID.</p>
<dt><code>photosets.comments.editComment</code> <i>COMMENT-ID TEXT</i></p>
<dd> Edit a photoset comment COMMENT-ID to have new TEXT.</p>
<dt><code>photosets.comments.getList</code> <i>PHOTOSET-ID</i></p>
<dd> Get the comments for a photoset PHOTOSET-ID.</p>
<dt><code>photosets.create</code> <i>TITLE DESCRIPTION PRIMARY-PHOTO-ID</i></p>
<dd> Create a photoset with TITLE, DESCRIPTION and PRIMARY-PHOTO-ID.</p>
<dt><code>photosets.delete</code> <i>PHOTOSET-ID</i></p>
<dd> Delete a photoset with PHOTOSET-ID.</p>
<dt><code>photosets.editMeta</code> <i>PHOTOSET-ID TITLE DESCRIPTION</i></p>
<dd> Set the TITLE and/or DESCRIPTION of a PHOTOSET-ID.</p>
<dt><code>photosets.editPhotos</code> <i>PHOTOSET-ID PRIMARY-PHOTO-ID PHOTO-IDS,&#8230;</i></p>
<dd> Set the PHOTO-IDs of a PHOTOSET-ID and PRIMARY-PHOTO-ID.</p>
<dt><code>photosets.getContext</code> <i>PHOTO-ID PHOTOSET-ID</i></p>
<dd> Get next and previous photos for PHOTO-ID in PHOTOSET-ID.</p>
<dt><code>photosets.getInfo</code> <i>PHOTOSET-ID</i></p>
<dd> Get information about PHOTOSET-ID.</p>
<dt><code>photosets.getList</code> <i>[USER-NSID]</i></p>
<dd> Get the list of photosets for the USER-NSID.</p>
<dt><code>photosets.getPhotos</code> <i>PHOTOSET-ID [EXTRAS [PRIVACY [PER-PAGE [PAGE [FORMAT]]]]]</i></p>
<dd> Get the list of photos in PHOTOSET-ID with options.</p>
<dt><code>photosets.orderSets</code> <i>PHOTOSET-IDS&#8230;</i></p>
<dd> Set the order of sets PHOTOSET-IDS.</p>
<dt><code>photosets.removePhoto</code> <i>PHOTOSET-ID PHOTO-ID</i></p>
<dd> Remove PHOTO-ID from PHOTOSET-ID.</p>
<dt><code>photosets.removePhotos</code> <i>PHOTOSET-ID PHOTO-IDS&#8230;</i></p>
<dd> Remove PHOTO-IDS from PHOTOSET-ID.</p>
<dt><code>photosets.reorderPhotos</code> <i>PHOTOSET-ID PHOTO-IDS&#8230;</i></p>
<dd> Reorder PHOTO-IDS from PHOTOSET-ID.</p>
<dt><code>photosets.setPrimaryPhoto</code> <i>PHOTOSET-ID PHOTO-ID</i></p>
<dd> Set photoset PHOTOSET-ID primary photo to PHOTO-ID.</p>
<dt><code>places.find</code> <i>TEXT</i></p>
<dd> Find places by TEXT query.</p>
<dt><code>places.findByLatLon</code> <i>LAT LON ACCURACY</i></p>
<dd> Find places by LAT and LON with ACCURACY 1-16.</p>
<dt><code>places.getChildrenWithPhotosPublic</code> <i>PLACE-ID|- [WOE-ID|-]</i></p>
<dd> Find child places with public photos by PLACE-ID or WOE-ID</p>
<dt><code>places.getInfo</code> <i>PLACE-ID|- [WOE-ID|-]</i></p>
<dd> Find place by PLACE-ID or WOE-ID</p>
<dt><code>places.getInfoByUrl</code> <i>URL</i></p>
<dd> Find place by place URL</p>
<dt><code>places.getPlaceTypes</code> <i>URL</i></p>
<dd> Get a list of available place types</p>
<dt><code>places.getShapeHistory</code> <i>PLACE-ID|- [WOE-ID|-]</i></p>
<dd> Get history of shapes for a place by PLACE-ID or WOE-ID</p>
<dt><code>places.getTopPlacesList</code> <i>PLACE-TYPE [DATE [WOE-ID|- [PLACE-ID]]]</i></p>
<dd> Get the top 100 most geotagged places for a DATE (or yesterday).</p>
<dt><code>places.placesForBoundingBox</code> <i>PLACE-TYPE MIN-LONG MIN-LAT MAX-LONG MAX-LAT</i></p>
<dd> Find user places of PLACE-TYPE in bbox.</p>
<dt><code>places.placesForContacts</code> <i>PLACE-TYPE WOE-ID|- PLACE-ID|- THRESHOLD [PARAMS]</i></p>
<dd> Find top 100 unique places clustered by a given PLACE-TYPE for a<br />
 user&#8217;s contacts with optional parameters<br />
 contacts CONTACTS<br />
 min-upload MIN-UPLOAD-DATE<br />
 max-upload MAX-UPLOAD-DATE<br />
 min-taken MIN-TAKEN-DATE<br />
 max-taken MAX-TAKEN-DATE</p>
<dt><code>places.placesForUser</code> <i>PLACE-TYPE [WOE-ID] [PLACE-ID [THRESHOLD]]]</i></p>
<dd> Find user places of PLACE-TYPE.</p>
<dt><code>places.resolvePlaceId</code> <i>PLACE-ID / WOE-ID</i></p>
<dd> Find places information by PLACE-ID or WOE-ID (number).</p>
<dt><code>places.resolvePlaceURL</code> <i>PLACE-URL</i></p>
<dd> Find places information by PLACE-URL.</p>
<dt><code>places.tagsForPlace</code> <i>PLACE-ID|- [WOE-ID|-]</i></p>
<dd> Get tags for a place by PLACE-ID or WOE-ID with optional parameters<br />
 min-upload MIN-UPLOAD-DATE<br />
 max-upload MAX-UPLOAD-DATE<br />
 min-taken MIN-TAKEN-DATE<br />
 max-taken MAX-TAKEN-DATE</p>
<dt><code>prefs.getContentType</code> <i></i></p>
<dd> Get default content type preference for user.</p>
<dt><code>prefs.getGeoPerms</code> <i></i></p>
<dd> Get default privacy level for geographic info for user.</p>
<dt><code>prefs.getHidden</code> <i></i></p>
<dd> Get default hidden preference for user.</p>
<dt><code>prefs.getPrivacy</code> <i></i></p>
<dd> Get default privacy preference for user.</p>
<dt><code>prefs.getSafetyLevel</code> <i></i></p>
<dd> Get default safety level for user.</p>
<dt><code>reflection.getMethodInfo</code> <i>NAME</i></p>
<dd> Get information about an API method NAME</p>
<dt><code>reflection.getMethods</code> <i></i></p>
<dd> Get API methods</p>
<dt><code>replace</code> <i>FILE PHOTO-ID [async]</i></p>
<dd> Replace a photo PHOTO-ID with a new FILE (async)</p>
<dt><code>shorturi</code> <i>PHOTO-ID</i></p>
<dd> Get the <a rel="nofollow" href="http://flic.kr">http://flic.kr</a> short uri for PHOTO-ID</p>
<dt><code>stats.getCollectionDomains</code> <i>DATE [COLLECTION-ID [PER-PAGE [PAGE]]]</i></p>
<dd> Get collection domains stats</p>
<dt><code>stats.getCollectionReferrers</code> <i>DATE DOMAIN [COLLECTION-ID [PER-PAGE [PAGE]]]</i></p>
<dd> Get collection referrers stats</p>
<dt><code>stats.getCollectionStats</code> <i>DATE COLLECTION-ID</i></p>
<dd> Get collection view count stats</p>
<dt><code>stats.getPhotoDomains</code> <i>DATE [PHOTO-ID [PER-PAGE [PAGE]]]</i></p>
<dd> Get photo domains stats</p>
<dt><code>stats.getPhotoReferrers</code> <i>DATE DOMAIN [PHOTO-ID [PER-PAGE [PAGE]]]</i></p>
<dd> Get photo referrers stats</p>
<dt><code>stats.getPhotoStats</code> <i>DATE PHOTO-ID</i></p>
<dd> Get photo view count stats</p>
<dt><code>stats.getPhotosetDomains</code> <i>DATE [PHOTOSET-ID [PER-PAGE [PAGE]]]</i></p>
<dd> Get photoset domains stats</p>
<dt><code>stats.getPhotosetReferrers</code> <i>DATE DOMAIN [PHOTOSET-ID [PER-PAGE [PAGE]]]</i></p>
<dd> Get photoset referrers stats</p>
<dt><code>stats.getPhotosetStats</code> <i>DATE PHOTOSET-ID</i></p>
<dd> Get photoset view count stats</p>
<dt><code>stats.getPhotostreamDomains</code> <i>DATE [PER-PAGE [PAGE]]</i></p>
<dd> Get photostream domains stats</p>
<dt><code>stats.getPhotostreamReferrers</code> <i>DATE DOMAIN [PER-PAGE [PAGE]]</i></p>
<dd> Get photostream referrers stats</p>
<dt><code>stats.getPhotostreamStats</code> <i>DATE</i></p>
<dd> Get photostream view count stats</p>
<dt><code>stats.getPopularPhotos</code> <i>[DATE [SORT [PER-PAGE [PAGE [EXTRAS]]]]]</i></p>
<dd> Get popular photos stats</p>
<dt><code>stats.getTotalViews</code> <i>[DATE]</i></p>
<dd> Get total stats</p>
<dt><code>tags.getClusters</code> <i>TAG</i></p>
<dd> Get list of tag clusters for TAG</p>
<dt><code>tags.getHotList</code> <i>[PERIOD [COUNT]]</i></p>
<dd> Get the list of hot tags for the given PERIOD (day, week)</p>
<dt><code>tags.getListPhoto</code> <i>PHOTO-ID</i></p>
<dd> Get the tag list for a PHOTO-ID.</p>
<dt><code>tags.getListUser</code> <i>[USER-NSID]</i></p>
<dd> Get the tag list for a USER-NSID (or current user).</p>
<dt><code>tags.getListUserPopular</code> <i>[USER-NSID [COUNT]]</i></p>
<dd> Get the popular tag list for a USER-NSID (or current user).</p>
<dt><code>tags.getListUserRaw</code> <i>[TAG]</i></p>
<dd> Get the raw versions of a TAG (or all tags) for the current user.</p>
<dt><code>tags.getMostFrequentlyUsed</code> <i></i></p>
<dd> Get the most frequently used tags for the current user.</p>
<dt><code>tags.getRelated</code> <i>TAG</i></p>
<dd> Get a list of tags &#8216;related&#8217; to TAG based on clustered usage analysis.</p>
<dt><code>test.echo</code> <i>KEY VALUE</i></p>
<dd> Test echo API call; echos KEY VALUE</p>
<dt><code>test.login</code> <i></i></p>
<dd> Test login API call: returns username</p>
<dt><code>test.null</code> <i>KEY VALUE</i></p>
<dd> Test null API call: no return</p>
<dt><code>upload</code> <i>FILE [PARAMS&#8230;]</i></p>
<dd> Upload a photo FILE with optional parameters PARAM or PARAM VALUE<br />
 title TITLE<br />
 description DESC<br />
 safety_level &#8216;safe&#8217; (default) or &#8216;moderate&#8217; or &#8216;restricted&#8217;<br />
 content_type &#8216;photo&#8217; (default) or screenshot&#8217; or &#8216;other&#8217;<br />
 hidden &#8216;public&#8217; (default) or &#8216;hidden&#8217;<br />
 friend<br />
 public<br />
 family<br />
 tags TAGS&#8230; [must be last param]</p>
<dt><code>urls.getGroup</code> <i>GROUP-ID</i></p>
<dd> Get the url of the group page for GROUP-ID.</p>
<dt><code>urls.getUserPhotos</code> <i>USER-NSID</i></p>
<dd> Get the url of the photo page for USER-NSID.</p>
<dt><code>urls.getUserProfile</code> <i>USER-NSID</i></p>
<dd> Get the url of the profile page for USER-NSID.</p>
<dt><code>urls.lookupGroup</code> <i>URL</i></p>
<dd> Get a group NSID from the URL to a group&#8217;s page or photo pool.</p>
<dt><code>urls.lookupUser</code> <i>URL</i></p>
<dd> Get a user NSID from the URL to a user&#8217;s photo</dl>
<h2>Extras Fields</h2>
<p> The <code>EXTRAS</code> parameter can take a comma-separated set of the following values</p>
<dl>
<dt><code>date_taken</code></p>
<dd> Date item was taken</p>
<dt><code>date_upload</code></p>
<dd> Date item was uploaded</p>
<dt><code>geo</code></p>
<dd> Geotagging latitude, longitude and accuracy</p>
<dt><code>icon_server</code></p>
<dd> Item owner icon fields</p>
<dt><code>last_update</code></p>
<dd> Date item was last updated</p>
<dt><code>license</code></p>
<dd> Item License</p>
<dt><code>machine_tags</code></p>
<dd> Machine tags</p>
<dt><code>media</code></p>
<dd> Item Format: photo or video</p>
<dt><code>o_dims</code></p>
<dd> Original item dimensions</p>
<dt><code>original_format</code></p>
<dd> Original item secret and format</p>
<dt><code>owner_name</code></p>
<dd> Item owner ID</p>
<dt><code>path_alias</code></p>
<dd> Path alias for owner like /photos/USERNAME</p>
<dt><code>tags</code></p>
<dd> Item clean tags (safe for HTML, URLs)</p>
<dt><code>url_m</code></p>
<dd> URL of medium size image</p>
<dt><code>url_o</code></p>
<dd> URL of original size image</p>
<dt><code>url_s</code></p>
<dd> URL of small size image</p>
<dt><code>url_sq</code></p>
<dd> URL of square size image</p>
<dt><code>url_t</code></p>
<dd> URL of thumbnail size image</p>
<dt><code>views</code></p>
<dd> Number of times item has been viewed</dl>
<h2>Photos List Feed Formats</h2>
<p> The <code>FORMAT</code> parameter can take any of the following values</p>
<dl>
<dt><code>feed-rss_100</code></p>
<dd> RSS 1.0</p>
<dt><code>feed-rss_200</code></p>
<dd> RSS 2.0</p>
<dt><code>feed-atom_10</code></p>
<dd> Atom 1.0</p>
<dt><code>feed-georss</code></p>
<dd> RSS 2.0 with GeoRSS and W3C Geo for geotagged photos</p>
<dt><code>feed-geoatom</code></p>
<dd> Atom 1.0 with GeoRSS and W3C Geo for geotagged photos</p>
<dt><code>feed-geordf</code></p>
<dd> RSS 1.0 with GeoRSS and W3C Geo for geotagged photos</p>
<dt><code>feed-kml</code></p>
<dd> KML 2.1</p>
<dt><code>feed-kml_nl</code></p>
<dd> KML 2.1 network link</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flickrdf/">flickrdf</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> flickcurl was written by David Beckett. </p>
<p> This manual page was written by Kumar Appaiah &lt;akumar [at] ee.iitm.ac.in&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
