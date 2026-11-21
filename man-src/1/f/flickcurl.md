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
<dt><code>-a </code><i>FROB</i>, &#8211;auth <i>FROB</i></dt>
<dd> Authenticate with a <i>FROB</i> and update the authentication file. The program will exit after updating the file.</dd>
<dt><code>-d </code><i>DELAY</i>, &#8211;delay <i>DELAY</i></dt>
<dd> Set delay between requests to <i>DELAY</i> milliseconds.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options and exit.</dd>
<dt><code>-o </code><i>FILE</i>, &#8211;output <i>FILE</i></dt>
<dd> Write the results of format feed API calls to <i>FILE</i></dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Display less information while the program runs.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Display the version of the program and exit.</dd>
<dt><code>-V, &#8211;verbose</code></dt>
<dd> Display more information while the program runs.</dd></dl>
<h2>COMMANDS</h2>
<p> In the following list of commands:<br />
 <i>PER-PAGE</i> is photos per result page or &#8216;-&#8216; for default (10)<br />
 <i>PAGE</i> is result page number or &#8216;-&#8216; for default (1 = first page) </p>
<dl>
<dt><code>activity.userComments</code> <i>[PER-PAGE [PAGE]]</i></dt>
<dd> Get photos commented on by the caller.</dd>
<dt><code>activity.userPhotos</code> <i>[TIMEFRAME [PER-PAGE [PAGE]]]</i></dt>
<dd> Get recent activity on the caller&#8217;s photos.</dd>
<dt><code>auth.checkToken</code> <i>TOKEN</i></dt>
<dd> Get the credentials attached to an authentication TOKEN.</dd>
<dt><code>auth.getFrob</code> <i></i></dt>
<dd> Get a frob to be used during authentication.</dd>
<dt><code>auth.getFullToken</code> <i>MINI-TOKEN</i></dt>
<dd> Get the full authentication token for MINI-TOKEN.</dd>
<dt><code>auth.getToken</code> <i>TOKEN</i></dt>
<dd> Get the auth token for the FROB, if one has been attached.</dd>
<dt><code>blogs.getList</code> <i></i></dt>
<dd> Get a list of configured blogs for the calling user.</dd>
<dt><code>blogs.getServices</code> <i></i></dt>
<dd> Get a list of blog services.</dd>
<dt><code>blogs.postPhoto</code> <i>BLOG-ID PHOTO-ID TITLE DESCRIPTION [BLOG-PASSWORD]</i></dt>
<dd> Post PHOTO-ID to blog BLOG-ID with TITLE, DESCRIPTION and optional password.</dd>
<dt><code>collections.getInfo</code> <i>COLLECTION-ID</i></dt>
<dd> Get information on collection COLLECTION-ID</dd>
<dt><code>collections.getTree</code> <i>[COLLECTION-ID|- [USER-ID|-]]</i></dt>
<dd> Get tree of collections COLLECTION-ID for USER-ID</dd>
<dt><code>commons.getInstitutions</code> <i></i></dt>
<dd> Get list of institutions</dd>
<dt><code>contacts.getList</code> <i>[FILTER [PAGE [PER-PAGE]]]</i></dt>
<dd> Get a list of contacts with optional FILTER</dd>
<dt><code>contacts.getListRecentlyUploaded</code> <i>[DATE-LAST-UPLOAD [FILTER]]</i></dt>
<dd> Get a list of recent uploading contacts since DATE-LAST-UPLOAD with optional FILTER</dd>
<dt><code>contacts.getPublicList</code> <i>USER-NSID [PAGE [PER-PAGE]]</i></dt>
<dd> Get the contact list for user USER-NSID</dd>
<dt><code>contacts.getTaggingSuggestions</code> <i>[PAGE [PER-PAGE [INCLUDE-SELF [INCLUDE-ADDRESS-BOOK]]]]</i></dt>
<dd> Get tagging suggestions</dd>
<dt><code>favorites.add</code> <i>PHOTO-ID</i></dt>
<dd> Adds PHOTO-ID to the current user&#8217;s favorites.</dd>
<dt><code>favorites.getContext</code> <i>PHOTO-ID USER-NSID [NUM-PREV [NUM-NEXT [EXTRAS]]]</i></dt>
<dd> Get context photos around USER-ID&#8217;s favorite PHOTO-ID.</dd>
<dt><code>favorites.getList</code> <i>USER-NSID [PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get a list of USER-NSID&#8217;s favorite photos.</dd>
<dt><code>favorites.getPublicList</code> <i>USER-NSID [PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get a list of USER-NSID&#8217;s favorite public photos.</dd>
<dt><code>favorites.remove</code> <i>PHOTO-ID</i></dt>
<dd> Removes PHOTO-ID to the current user&#8217;s favorites.</dd>
<dt><code>galleries.addPhoto</code> <i>GALLERY-ID PHOTO-ID TEXT</i></dt>
<dd> Add photo PHOTO-ID to galleries GALLERY-ID with TEXT</dd>
<dt><code>galleries.create</code> <i>TITLE [DESCRIPTION [PRIMARY-PHOTO-ID]</i></dt>
<dd> Create a new gallery with TITLE, DESCRIPTION and PRIMARY-PHOTO_ID.</dd>
<dt><code>galleries.editMeta</code> <i>GALLERY-ID TITLE [DESCRIPTION]</i></dt>
<dd> Set the TITLE and/or DESCRIPTION of a GALLERY-ID.</dd>
<dt><code>galleries.editPhoto</code> <i>GALLERY-ID PHOTO-ID COMMENT</i></dt>
<dd> Set the COMMENT for PHOTO-ID in GALLERY-ID.</dd>
<dt><code>galleries.editPhotos</code> <i>GALLERY-ID PRIMARY-PHOTO-ID PHOTO-IDS,&#8230;</i></dt>
<dd> Set the PHOTO-IDs of a GALLERY-ID and PRIMARY-PHOTO-ID.</dd>
<dt><code>galleries.getInfo</code> <i>GALLERY-ID</i></dt>
<dd> Get information about GALLERY-ID.</dd>
<dt><code>galleries.getList</code> <i>USER-ID [PER-PAGE [PAGE]]</i></dt>
<dd> Get list of galleries for a USER-ID with optional paging</dd>
<dt><code>galleries.getListForPhoto</code> <i>PHOTO-ID [PER-PAGE [PAGE]]</i></dt>
<dd> Get list of galleries PHOTO-ID appears in with optional paging</dd>
<dt><code>galleries.getPhotos</code> <i>GALLERY-ID [EXTRAS [PER-PAGE [PAGE [FORMAT]]]]</i></dt>
<dd> Get the list of photos in GALLERY-ID with options.</dd>
<dt><code>getphotoid</code> <i>IMAGE-URL</i></dt>
<dd> Get the photo id from a raw flickr farm IMAGE-URL</dd>
<dt><code>groups.browse</code> <i>[CAT-ID]</i></dt>
<dd> Browse groups below category CAT-ID (or root).</dd>
<dt><code>groups.getInfo</code> <i>GROUP-ID [LANG]</i></dt>
<dd> Get information on group GROUP-ID with language LANG.</dd>
<dt><code>groups.join</code> <i>GROUP-ID [ACCEPT-RULES]</i></dt>
<dd> Join a group GROUP-ID with optional accepting of rules.</dd>
<dt><code>groups.joinRequest</code> <i>GROUP-ID MESSAGE ACCEPT-RULES</i></dt>
<dd> Request to join a group GROUP-ID using MESSAGE and accept rules.</dd>
<dt><code>groups.leave</code> <i>GROUP-ID [DELETE-PHOTOS]</i></dt>
<dd> Leave a group GROUP-ID and optionally delete photos.</dd>
<dt><code>groups.members.getList</code> <i>GROUP-ID [MEMBER-TYPES [PER-PAGE [PAGE]]]</i></dt>
<dd> Get list of MEMBER-TYPES types members of group GROUP-ID.</dd>
<dt><code>groups.pools.add</code> <i>PHOTO-ID GROUP-ID</i></dt>
<dd> Add PHOTO-ID in GROUP-ID pool.</dd>
<dt><code>groups.pools.getContext</code> <i>PHOTO-ID GROUP-ID</i></dt>
<dd> Get next and previous photos for PHOTO-ID in GROUP-ID pool.</dd>
<dt><code>groups.pools.getGroups</code> <i>[PER-PAGE [PAGE]]</i></dt>
<dd> Get list of groups a user can add to.</dd>
<dt><code>groups.pools.getPhotos</code> <i>GROUP-ID [PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get list of photos in GROUP-ID.</dd>
<dt><code>groups.pools.remove</code> <i>PHOTO-ID GROUP-ID</i></dt>
<dd> Remove PHOTO-ID from group GROUP-ID.</dd>
<dt><code>groups.search</code> <i>TEXT [PER-PAGE [PAGE]]</i></dt>
<dd> Search for groups matching TEXT paging PER-PAGE and PAGE.</dd>
<dt><code>interestingness.getList</code> <i>[PARAMS]</i></dt>
<dd> Get interesting photos with optional parameters<br />
 date DATE<br />
 extras EXTRAS<br />
 per-page PER-PAGE<br />
 page PAGE<br />
 format FORMAT</dd>
<dt><code>machinetags.getNamespaces</code> <i>[PREDICATE [PER-PAGE [PAGE]]]</i></dt>
<dd> Get a list of namespaces with optional PREDICATE</dd>
<dt><code>machinetags.getPairs</code> <i>[NAMESPACE [PREDICATE [PER-PAGE [PAGE]]]]</i></dt>
<dd> Get a list of unique NAMESPACE and PREDICATE pairs</dd>
<dt><code>machinetags.getPredicates</code> <i>[NAMESPACE [PER-PAGE [PAGE]]]</i></dt>
<dd> Get a list of unique predicates optionally by NAMESPACE</dd>
<dt><code>machinetags.getRecentValues</code> <i>[NAMESPACE|- [PREDICATE|- [ADDED-SINCE]]]</i></dt>
<dd> Get a list of recent machinetags for NAMESPACE and PREDICATE since ADDED-SINCE</dd>
<dt><code>machinetags.getValues</code> <i>NAMESPACE PREDICATE [PER-PAGE [PAGE]]</i></dt>
<dd> Get a list of unique values for a NAMESPACE and PREDICATE</dd>
<dt><code>oauth.create</code> <i>[CALLBACK]</i></dt>
<dd> Create OAuth request token/secret pair and show the authentication URL</dd>
<dt><code>oauth.upgrade</code> <i></i></dt>
<dd> Upgrade legacy authentication to OAuth</dd>
<dt><code>oauth.verify</code> <i>REQUEST-TOKEN REQUEST-TOKEN-SECRET VERIFIER</i></dt>
<dd> Verify an OAuth request from `oauth.create&#8217;</dd>
<dt><code>panda.getList</code> <i></i></dt>
<dd> get the current list of pandas</dd>
<dt><code>panda.getPhotos</code> <i>PANDA</i></dt>
<dd> ask a PANDA for a list of recent public and safe photos</dd>
<dt><code>people.findByEmail</code> <i>EMAIL</i></dt>
<dd> get a user&#8217;s NSID from their EMAIL address</dd>
<dt><code>people.findByUsername</code> <i>USERNAME</i></dt>
<dd> get a user&#8217;s NSID from their USERNAME</dd>
<dt><code>people.getGroups</code> <i>USER-ID [GROUP-EXTRAS]</i></dt>
<dd> Get list of groups USER-ID is a member of</dd>
<dt><code>people.getInfo</code> <i>USER-NSID</i></dt>
<dd> Get information about one person with id USER-NSID</dd>
<dt><code>people.getPhotos</code> <i>USER-NSID</i></dt>
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
 format FORMAT</dd>
<dt><code>people.getPhotosOf</code> <i>USER-NSID [PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get public photos of a user USER-NSID</dd>
<dt><code>people.getPublicGroups</code> <i>USER-NSID</i></dt>
<dd> Get list of public groups a user is a member of</dd>
<dt><code>people.getPublicPhotos</code> <i>USER-NSID [PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get public photos for a user USER-NSID</dd>
<dt><code>people.getUploadStatus</code> <i></i></dt>
<dd> Get calling user upload status</dd>
<dt><code>photos.addTags</code> <i>PHOTO-ID TAGS</i></dt>
<dd> Add TAGS to a PHOTO-ID.</dd>
<dt><code>photos.comments.addComment</code> <i>PHOTO-ID TEXT</i></dt>
<dd> Add a photo comment TEXT to PHOTO-ID.</dd>
<dt><code>photos.comments.deleteComment</code> <i>COMMENT-ID</i></dt>
<dd> Delete a photo comment COMMENT-ID.</dd>
<dt><code>photos.comments.editComment</code> <i>COMMENT-ID TEXT</i></dt>
<dd> Edit a photo comment COMMENT-ID to have new TEXT.</dd>
<dt><code>photos.comments.getList</code> <i>PHOTO-ID</i></dt>
<dd> Get the comments for a photo PHOTO-ID.</dd>
<dt><code>photos.comments.getRecentForContacts</code> <i>[PARAMS]</i></dt>
<dd> Get the list of photos for user contacts with recent comments<br />
 since DATE-LAST-COMMENT filter CONTACTS-FILTER<br />
 per-page PER-PAGE page PAGE format FORMAT</dd>
<dt><code>photos.delete</code> <i>PHOTO-ID</i></dt>
<dd> Delete a PHOTO-ID.</dd>
<dt><code>photos.geo.getLocation</code> <i>PHOTO-ID</i></dt>
<dd> Get the geo location for a photo PHOTO-ID.</dd>
<dt><code>photos.geo.getPerms</code> <i>PHOTO-ID</i></dt>
<dd> Get the geo perms for a photo PHOTO-ID.</dd>
<dt><code>photos.geo.removeLocation</code> <i>PHOTO-ID</i></dt>
<dd> Remove the location for a photo PHOTO-ID.</dd>
<dt><code>photos.geo.setLocation</code> <i>PHOTO-ID LAT LONG ACCURACY</i></dt>
<dd> Set the location for a photo PHOTO-ID.</dd>
<dt><code>photos.geo.setPerms</code> <i>PHOTO-ID IS-PUBLIC IS-CONTACT IS-FRIEND IS-FAMILY</i></dt>
<dd> Set the geo perms for a photo PHOTO-ID.</dd>
<dt><code>photos.getAllContexts</code> <i>PHOTO-ID</i></dt>
<dd> Get all visible sets and pools the PHOTO-ID belongs to.</dd>
<dt><code>photos.getContactsPhotos</code> <i></i></dt>
<dd> Get a list of recent photos from the calling users&#8217; contacts</dd>
<dt><code>photos.getContactsPublicPhotos</code> <i>USER-NSID [FORMAT]</i></dt>
<dd> Get a list of recent public photos from USER-NSID&#8217;s contacts</dd>
<dt><code>photos.getContext</code> <i>PHOTO-ID</i></dt>
<dd> Get next and previous photos for a PHOTO-ID in a photostream.</dd>
<dt><code>photos.getCounts</code> <i>DATES TAKEN-DATES</i></dt>
<dd> Get the counts for a set of DATES or TAKEN-DATES.</dd>
<dt><code>photos.getExif</code> <i>PHOTO-ID</i></dt>
<dd> Get EXIF information about one photo with id PHOTO-ID</dd>
<dt><code>photos.getFavorites</code> <i>PHOTO-ID [PER-PAGE [PAGE]]</i></dt>
<dd> Get favourites information about one photo with id PHOTO-ID</dd>
<dt><code>photos.getInfo</code> <i>PHOTO-ID [SECRET]</i></dt>
<dd> Get information about one photo PHOTO-ID with optional SECRET</dd>
<dt><code>photos.getNotInSet</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get list of photos that are not in any set</dd>
<dt><code>photos.getPerms</code> <i>PHOTO-ID</i></dt>
<dd> Get a photo viewing and commenting permissions</dd>
<dt><code>photos.getRecent</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get list of recent photos</dd>
<dt><code>photos.getSizes</code> <i>PHOTO-ID</i></dt>
<dd> Get sizes of a PHOTO-ID</dd>
<dt><code>photos.getUntagged</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get list of photos that are not tagged</dd>
<dt><code>photos.getWithGeoData</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get list of photos that have geo data</dd>
<dt><code>photos.getWithoutGeoData</code> <i>[PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get list of photos that do not have geo data</dd>
<dt><code>photos.licenses.getInfo</code> <i></i></dt>
<dd> Get list of available photo licenses</dd>
<dt><code>photos.licenses.setLicense</code> <i>PHOTO-ID LICENSE-ID</i></dt>
<dd> Get photo PHOTO-ID license to LICENSE-ID</dd>
<dt><code>photos.notes.add</code> <i>PHOTO-ID X Y W H TEXT</i></dt>
<dd> Add a note (X, Y, W, H, TEXT) to a photo with id PHOTO-ID</dd>
<dt><code>photos.notes.delete</code> <i>NOTE-ID</i></dt>
<dd> Delete a note with id NOTE-ID</dd>
<dt><code>photos.notes.edit</code> <i>NOTE-ID X Y W H TEXT</i></dt>
<dd> Edit note NOTE-ID to (X, Y, W, H, TEXT)</dd>
<dt><code>photos.people.add</code> <i>PHOTO-ID USER-ID X Y W H</i></dt>
<dd> Mark USER-ID appearing in PHOTO-ID at (X, Y, W, H)</dd>
<dt><code>photos.people.delete</code> <i>PHOTO-ID USER-ID</i></dt>
<dd> Mark USER-ID as not appearing in PHOTO-ID</dd>
<dt><code>photos.people.deleteCoords</code> <i>PHOTO-ID USER-ID</i></dt>
<dd> Mark USER-ID as not appearing at coordinates in PHOTO-ID</dd>
<dt><code>photos.people.editCoords</code> <i>PHOTO-ID USER-ID X Y W H</i></dt>
<dd> Update USER-ID appearing in PHOTO-ID to coords (X, Y, W, H)</dd>
<dt><code>photos.people.getList</code> <i>PHOTO-ID</i></dt>
<dd> Get list of users appearing in PHOTO-ID</dd>
<dt><code>photos.recentlyUpdated</code> <i>MIN-DATE [PER-PAGE [PAGE [FORMAT]]]</i></dt>
<dd> Get list of photos that were recently updated</dd>
<dt><code>photos.removeTag</code> <i>PHOTO-ID TAG-ID</i></dt>
<dd> Remove a tag TAG-ID from a photo.</dd>
<dt><code>photos.search</code> <i>[PARAMS] tags TAGS&#8230;</i></dt>
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
 in-gallery</dd>
<dt><code>photos.setContentType</code> <i>PHOTO-ID TYPE</i></dt>
<dd> Set photo TYPE to one of &#8216;photo&#8217;, &#8216;screenshot&#8217; or &#8216;other&#8217;</dd>
<dt><code>photos.setDates</code> <i>PHOTO-ID POSTED TAKEN GRANULARITY</i></dt>
<dd> Set a photo POSTED date, TAKEN date with GRANULARITY</dd>
<dt><code>photos.setMeta</code> <i>PHOTO-ID TITLE DESCRIPTION</i></dt>
<dd> Set a photo TITLE and DESCRIPTION</dd>
<dt><code>photos.setPerms</code> <i>PHOTO-ID IS-PUBLIC IS-FRIEND IS-FAMILY PERM-COMMENT PERM-ADDMETA</i></dt>
<dd> Set a photo viewing and commenting permissions</dd>
<dt><code>photos.setSafetyLevel</code> <i>PHOTO-ID SAFETY-LEVEL HIDDEN</i></dt>
<dd> Set a photo&#8217;s SAFETY-LEVEL and HIDDEN flag</dd>
<dt><code>photos.setTags</code> <i>PHOTO-ID TAGS</i></dt>
<dd> Set the tags for a PHOTO-ID to TAGS.</dd>
<dt><code>photos.transform.rotate</code> <i>PHOTO-ID DEGREES</i></dt>
<dd> Rotate PHOTO-ID by 90/180/270 DEGREES</dd>
<dt><code>photos.upload.checkTickets</code> <i>TICKET-IDS&#8230;</i></dt>
<dd> Get the status of upload TICKET-IDS</dd>
<dt><code>photosets.addPhoto</code> <i>PHOTOSET-ID PHOTO-ID</i></dt>
<dd> Add PHOTO-ID to a PHOTOSET-ID.</dd>
<dt><code>photosets.comments.addComment</code> <i>PHOTOSET-ID TEXT</i></dt>
<dd> Add a comment TEXT to photoset PHOTOSET-ID.</dd>
<dt><code>photosets.comments.deleteComment</code> <i>COMMENT-ID</i></dt>
<dd> Delete a photoset comment COMMENT-ID.</dd>
<dt><code>photosets.comments.editComment</code> <i>COMMENT-ID TEXT</i></dt>
<dd> Edit a photoset comment COMMENT-ID to have new TEXT.</dd>
<dt><code>photosets.comments.getList</code> <i>PHOTOSET-ID</i></dt>
<dd> Get the comments for a photoset PHOTOSET-ID.</dd>
<dt><code>photosets.create</code> <i>TITLE DESCRIPTION PRIMARY-PHOTO-ID</i></dt>
<dd> Create a photoset with TITLE, DESCRIPTION and PRIMARY-PHOTO-ID.</dd>
<dt><code>photosets.delete</code> <i>PHOTOSET-ID</i></dt>
<dd> Delete a photoset with PHOTOSET-ID.</dd>
<dt><code>photosets.editMeta</code> <i>PHOTOSET-ID TITLE DESCRIPTION</i></dt>
<dd> Set the TITLE and/or DESCRIPTION of a PHOTOSET-ID.</dd>
<dt><code>photosets.editPhotos</code> <i>PHOTOSET-ID PRIMARY-PHOTO-ID PHOTO-IDS,&#8230;</i></dt>
<dd> Set the PHOTO-IDs of a PHOTOSET-ID and PRIMARY-PHOTO-ID.</dd>
<dt><code>photosets.getContext</code> <i>PHOTO-ID PHOTOSET-ID</i></dt>
<dd> Get next and previous photos for PHOTO-ID in PHOTOSET-ID.</dd>
<dt><code>photosets.getInfo</code> <i>PHOTOSET-ID</i></dt>
<dd> Get information about PHOTOSET-ID.</dd>
<dt><code>photosets.getList</code> <i>[USER-NSID]</i></dt>
<dd> Get the list of photosets for the USER-NSID.</dd>
<dt><code>photosets.getPhotos</code> <i>PHOTOSET-ID [EXTRAS [PRIVACY [PER-PAGE [PAGE [FORMAT]]]]]</i></dt>
<dd> Get the list of photos in PHOTOSET-ID with options.</dd>
<dt><code>photosets.orderSets</code> <i>PHOTOSET-IDS&#8230;</i></dt>
<dd> Set the order of sets PHOTOSET-IDS.</dd>
<dt><code>photosets.removePhoto</code> <i>PHOTOSET-ID PHOTO-ID</i></dt>
<dd> Remove PHOTO-ID from PHOTOSET-ID.</dd>
<dt><code>photosets.removePhotos</code> <i>PHOTOSET-ID PHOTO-IDS&#8230;</i></dt>
<dd> Remove PHOTO-IDS from PHOTOSET-ID.</dd>
<dt><code>photosets.reorderPhotos</code> <i>PHOTOSET-ID PHOTO-IDS&#8230;</i></dt>
<dd> Reorder PHOTO-IDS from PHOTOSET-ID.</dd>
<dt><code>photosets.setPrimaryPhoto</code> <i>PHOTOSET-ID PHOTO-ID</i></dt>
<dd> Set photoset PHOTOSET-ID primary photo to PHOTO-ID.</dd>
<dt><code>places.find</code> <i>TEXT</i></dt>
<dd> Find places by TEXT query.</dd>
<dt><code>places.findByLatLon</code> <i>LAT LON ACCURACY</i></dt>
<dd> Find places by LAT and LON with ACCURACY 1-16.</dd>
<dt><code>places.getChildrenWithPhotosPublic</code> <i>PLACE-ID|- [WOE-ID|-]</i></dt>
<dd> Find child places with public photos by PLACE-ID or WOE-ID</dd>
<dt><code>places.getInfo</code> <i>PLACE-ID|- [WOE-ID|-]</i></dt>
<dd> Find place by PLACE-ID or WOE-ID</dd>
<dt><code>places.getInfoByUrl</code> <i>URL</i></dt>
<dd> Find place by place URL</dd>
<dt><code>places.getPlaceTypes</code> <i>URL</i></dt>
<dd> Get a list of available place types</dd>
<dt><code>places.getShapeHistory</code> <i>PLACE-ID|- [WOE-ID|-]</i></dt>
<dd> Get history of shapes for a place by PLACE-ID or WOE-ID</dd>
<dt><code>places.getTopPlacesList</code> <i>PLACE-TYPE [DATE [WOE-ID|- [PLACE-ID]]]</i></dt>
<dd> Get the top 100 most geotagged places for a DATE (or yesterday).</dd>
<dt><code>places.placesForBoundingBox</code> <i>PLACE-TYPE MIN-LONG MIN-LAT MAX-LONG MAX-LAT</i></dt>
<dd> Find user places of PLACE-TYPE in bbox.</dd>
<dt><code>places.placesForContacts</code> <i>PLACE-TYPE WOE-ID|- PLACE-ID|- THRESHOLD [PARAMS]</i></dt>
<dd> Find top 100 unique places clustered by a given PLACE-TYPE for a<br />
 user&#8217;s contacts with optional parameters<br />
 contacts CONTACTS<br />
 min-upload MIN-UPLOAD-DATE<br />
 max-upload MAX-UPLOAD-DATE<br />
 min-taken MIN-TAKEN-DATE<br />
 max-taken MAX-TAKEN-DATE</dd>
<dt><code>places.placesForUser</code> <i>PLACE-TYPE [WOE-ID] [PLACE-ID [THRESHOLD]]]</i></dt>
<dd> Find user places of PLACE-TYPE.</dd>
<dt><code>places.resolvePlaceId</code> <i>PLACE-ID / WOE-ID</i></dt>
<dd> Find places information by PLACE-ID or WOE-ID (number).</dd>
<dt><code>places.resolvePlaceURL</code> <i>PLACE-URL</i></dt>
<dd> Find places information by PLACE-URL.</dd>
<dt><code>places.tagsForPlace</code> <i>PLACE-ID|- [WOE-ID|-]</i></dt>
<dd> Get tags for a place by PLACE-ID or WOE-ID with optional parameters<br />
 min-upload MIN-UPLOAD-DATE<br />
 max-upload MAX-UPLOAD-DATE<br />
 min-taken MIN-TAKEN-DATE<br />
 max-taken MAX-TAKEN-DATE</dd>
<dt><code>prefs.getContentType</code> <i></i></dt>
<dd> Get default content type preference for user.</dd>
<dt><code>prefs.getGeoPerms</code> <i></i></dt>
<dd> Get default privacy level for geographic info for user.</dd>
<dt><code>prefs.getHidden</code> <i></i></dt>
<dd> Get default hidden preference for user.</dd>
<dt><code>prefs.getPrivacy</code> <i></i></dt>
<dd> Get default privacy preference for user.</dd>
<dt><code>prefs.getSafetyLevel</code> <i></i></dt>
<dd> Get default safety level for user.</dd>
<dt><code>reflection.getMethodInfo</code> <i>NAME</i></dt>
<dd> Get information about an API method NAME</dd>
<dt><code>reflection.getMethods</code> <i></i></dt>
<dd> Get API methods</dd>
<dt><code>replace</code> <i>FILE PHOTO-ID [async]</i></dt>
<dd> Replace a photo PHOTO-ID with a new FILE (async)</dd>
<dt><code>shorturi</code> <i>PHOTO-ID</i></dt>
<dd> Get the <a rel="nofollow" href="http://flic.kr">http://flic.kr</a> short uri for PHOTO-ID</dd>
<dt><code>stats.getCollectionDomains</code> <i>DATE [COLLECTION-ID [PER-PAGE [PAGE]]]</i></dt>
<dd> Get collection domains stats</dd>
<dt><code>stats.getCollectionReferrers</code> <i>DATE DOMAIN [COLLECTION-ID [PER-PAGE [PAGE]]]</i></dt>
<dd> Get collection referrers stats</dd>
<dt><code>stats.getCollectionStats</code> <i>DATE COLLECTION-ID</i></dt>
<dd> Get collection view count stats</dd>
<dt><code>stats.getPhotoDomains</code> <i>DATE [PHOTO-ID [PER-PAGE [PAGE]]]</i></dt>
<dd> Get photo domains stats</dd>
<dt><code>stats.getPhotoReferrers</code> <i>DATE DOMAIN [PHOTO-ID [PER-PAGE [PAGE]]]</i></dt>
<dd> Get photo referrers stats</dd>
<dt><code>stats.getPhotoStats</code> <i>DATE PHOTO-ID</i></dt>
<dd> Get photo view count stats</dd>
<dt><code>stats.getPhotosetDomains</code> <i>DATE [PHOTOSET-ID [PER-PAGE [PAGE]]]</i></dt>
<dd> Get photoset domains stats</dd>
<dt><code>stats.getPhotosetReferrers</code> <i>DATE DOMAIN [PHOTOSET-ID [PER-PAGE [PAGE]]]</i></dt>
<dd> Get photoset referrers stats</dd>
<dt><code>stats.getPhotosetStats</code> <i>DATE PHOTOSET-ID</i></dt>
<dd> Get photoset view count stats</dd>
<dt><code>stats.getPhotostreamDomains</code> <i>DATE [PER-PAGE [PAGE]]</i></dt>
<dd> Get photostream domains stats</dd>
<dt><code>stats.getPhotostreamReferrers</code> <i>DATE DOMAIN [PER-PAGE [PAGE]]</i></dt>
<dd> Get photostream referrers stats</dd>
<dt><code>stats.getPhotostreamStats</code> <i>DATE</i></dt>
<dd> Get photostream view count stats</dd>
<dt><code>stats.getPopularPhotos</code> <i>[DATE [SORT [PER-PAGE [PAGE [EXTRAS]]]]]</i></dt>
<dd> Get popular photos stats</dd>
<dt><code>stats.getTotalViews</code> <i>[DATE]</i></dt>
<dd> Get total stats</dd>
<dt><code>tags.getClusters</code> <i>TAG</i></dt>
<dd> Get list of tag clusters for TAG</dd>
<dt><code>tags.getHotList</code> <i>[PERIOD [COUNT]]</i></dt>
<dd> Get the list of hot tags for the given PERIOD (day, week)</dd>
<dt><code>tags.getListPhoto</code> <i>PHOTO-ID</i></dt>
<dd> Get the tag list for a PHOTO-ID.</dd>
<dt><code>tags.getListUser</code> <i>[USER-NSID]</i></dt>
<dd> Get the tag list for a USER-NSID (or current user).</dd>
<dt><code>tags.getListUserPopular</code> <i>[USER-NSID [COUNT]]</i></dt>
<dd> Get the popular tag list for a USER-NSID (or current user).</dd>
<dt><code>tags.getListUserRaw</code> <i>[TAG]</i></dt>
<dd> Get the raw versions of a TAG (or all tags) for the current user.</dd>
<dt><code>tags.getMostFrequentlyUsed</code> <i></i></dt>
<dd> Get the most frequently used tags for the current user.</dd>
<dt><code>tags.getRelated</code> <i>TAG</i></dt>
<dd> Get a list of tags &#8216;related&#8217; to TAG based on clustered usage analysis.</dd>
<dt><code>test.echo</code> <i>KEY VALUE</i></dt>
<dd> Test echo API call; echos KEY VALUE</dd>
<dt><code>test.login</code> <i></i></dt>
<dd> Test login API call: returns username</dd>
<dt><code>test.null</code> <i>KEY VALUE</i></dt>
<dd> Test null API call: no return</dd>
<dt><code>upload</code> <i>FILE [PARAMS&#8230;]</i></dt>
<dd> Upload a photo FILE with optional parameters PARAM or PARAM VALUE<br />
 title TITLE<br />
 description DESC<br />
 safety_level &#8216;safe&#8217; (default) or &#8216;moderate&#8217; or &#8216;restricted&#8217;<br />
 content_type &#8216;photo&#8217; (default) or screenshot&#8217; or &#8216;other&#8217;<br />
 hidden &#8216;public&#8217; (default) or &#8216;hidden&#8217;<br />
 friend<br />
 public<br />
 family<br />
 tags TAGS&#8230; [must be last param]</dd>
<dt><code>urls.getGroup</code> <i>GROUP-ID</i></dt>
<dd> Get the url of the group page for GROUP-ID.</dd>
<dt><code>urls.getUserPhotos</code> <i>USER-NSID</i></dt>
<dd> Get the url of the photo page for USER-NSID.</dd>
<dt><code>urls.getUserProfile</code> <i>USER-NSID</i></dt>
<dd> Get the url of the profile page for USER-NSID.</dd>
<dt><code>urls.lookupGroup</code> <i>URL</i></dt>
<dd> Get a group NSID from the URL to a group&#8217;s page or photo pool.</dd>
<dt><code>urls.lookupUser</code> <i>URL</i></dt>
<dd> Get a user NSID from the URL to a user&#8217;s photo</dd></dl>
<h2>Extras Fields</h2>
<p> The <code>EXTRAS</code> parameter can take a comma-separated set of the following values</p>
<dl>
<dt><code>date_taken</code></dt>
<dd> Date item was taken</dd>
<dt><code>date_upload</code></dt>
<dd> Date item was uploaded</dd>
<dt><code>geo</code></dt>
<dd> Geotagging latitude, longitude and accuracy</dd>
<dt><code>icon_server</code></dt>
<dd> Item owner icon fields</dd>
<dt><code>last_update</code></dt>
<dd> Date item was last updated</dd>
<dt><code>license</code></dt>
<dd> Item License</dd>
<dt><code>machine_tags</code></dt>
<dd> Machine tags</dd>
<dt><code>media</code></dt>
<dd> Item Format: photo or video</dd>
<dt><code>o_dims</code></dt>
<dd> Original item dimensions</dd>
<dt><code>original_format</code></dt>
<dd> Original item secret and format</dd>
<dt><code>owner_name</code></dt>
<dd> Item owner ID</dd>
<dt><code>path_alias</code></dt>
<dd> Path alias for owner like /photos/USERNAME</dd>
<dt><code>tags</code></dt>
<dd> Item clean tags (safe for HTML, URLs)</dd>
<dt><code>url_m</code></dt>
<dd> URL of medium size image</dd>
<dt><code>url_o</code></dt>
<dd> URL of original size image</dd>
<dt><code>url_s</code></dt>
<dd> URL of small size image</dd>
<dt><code>url_sq</code></dt>
<dd> URL of square size image</dd>
<dt><code>url_t</code></dt>
<dd> URL of thumbnail size image</dd>
<dt><code>views</code></dt>
<dd> Number of times item has been viewed</dd></dl>
<h2>Photos List Feed Formats</h2>
<p> The <code>FORMAT</code> parameter can take any of the following values</p>
<dl>
<dt><code>feed-rss_100</code></dt>
<dd> RSS 1.0</dd>
<dt><code>feed-rss_200</code></dt>
<dd> RSS 2.0</dd>
<dt><code>feed-atom_10</code></dt>
<dd> Atom 1.0</dd>
<dt><code>feed-georss</code></dt>
<dd> RSS 2.0 with GeoRSS and W3C Geo for geotagged photos</dd>
<dt><code>feed-geoatom</code></dt>
<dd> Atom 1.0 with GeoRSS and W3C Geo for geotagged photos</dd>
<dt><code>feed-geordf</code></dt>
<dd> RSS 1.0 with GeoRSS and W3C Geo for geotagged photos</dd>
<dt><code>feed-kml</code></dt>
<dd> KML 2.1</dd>
<dt><code>feed-kml_nl</code></dt>
<dd> KML 2.1 network link</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flickrdf/">flickrdf</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> flickcurl was written by David Beckett. </p>
<p> This manual page was written by Kumar Appaiah &lt;akumar [at] ee.iitm.ac.in&gt;, for the Debian project (but may be used by others). </p>
