---
title: "google(1)"
name: "google"
section: "1"
letter: "g"
url: "/docs/linux/man/1-google/"
description: "google – command-line access to (some) Google services"
---

<h2>NAME</h2>
<p> google &#8211; command-line access to (some) Google services</p>
<h2>SYNOPSIS</h2>
<p> <code>google</code> [<i>picasa|blogger|youtube|docs|contacts|calendar</i>] <i>TASK </i>[<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> This program provides command-line access to (some) google services via their gdata APIs. Called without a service name, it starts an interactive session. </p>
<p> Available tasks for service picasa: &#8216;get&#8217;, &#8216;create&#8217;, &#8216;list&#8217;, &#8216;list-albums&#8217;, &#8216;tag&#8217;, &#8216;post&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
</dt><dd> get: Download albums</dd>
<dt>
</dt><dd> Requires: none Optional: title, owner, format Arguments: LOCATION</dd>
<dt>
</dt><dd> create: Create an album</dd>
<dt>
</dt><dd> Requires: title Optional: date, summary, tags Arguments: PATH_TO_PHOTOS</dd>
<dt>
</dt><dd> list: List photos</dd>
<dt>
</dt><dd> Requires: delimiter Optional: title, query, owner</dd>
<dt>
</dt><dd> list-albums: List albums</dd>
<dt>
</dt><dd> Requires: delimiter Optional: title, owner</dd>
<dt>
</dt><dd> tag: Tag photos</dd>
<dt>
</dt><dd> Requires: tags AND (title OR query) Optional: owner</dd>
<dt>
</dt><dd> post: Post photos to an album</dd>
<dt>
</dt><dd> Requires: title Optional: tags, owner Arguments: PATH_TO_PHOTOS</dd>
<dt>
</dt><dd> delete: Delete photos or albums</dd>
<dt>
</dt><dd> Requires: (title OR query)</dd></dl>
<p> Available tasks for service blogger: &#8216;post&#8217;, &#8216;tag&#8217;, &#8216;list&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
</dt><dd> post: Post content.</dd>
<dt>
</dt><dd> Requires: none Optional: blog, title, tags Arguments: PATH_TO_CONTENT or CONTENT</dd>
<dt>
</dt><dd> tag: Label posts</dd>
<dt>
</dt><dd> Requires: tags AND title Optional: blog</dd>
<dt>
</dt><dd> list: List posts in a blog</dd>
<dt>
</dt><dd> Requires: delimiter Optional: blog, title, owner</dd>
<dt>
</dt><dd> delete: Delete a post.</dd>
<dt>
</dt><dd> Requires: title Optional: blog</dd></dl>
<p> Available tasks for service youtube: &#8216;post&#8217;, &#8216;tag&#8217;, &#8216;list&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
</dt><dd> post: Post a video.</dd>
<dt>
</dt><dd> Requires: category AND devkey Optional: title, summary, tags Arguments: PATH_TO_VIDEO</dd>
<dt>
</dt><dd> tag: Add tags to a video and/or change its category.</dd>
<dt>
</dt><dd> Requires: devkey AND title AND (category OR tags)</dd>
<dt>
</dt><dd> list: List videos by user.</dd>
<dt>
</dt><dd> Requires: delimiter Optional: title, owner</dd>
<dt>
</dt><dd> delete: Delete videos.</dd>
<dt>
</dt><dd> Requires: devkey Optional: title</dd></dl>
<p> Available tasks for service docs: &#8216;edit&#8217;, &#8216;delete&#8217;, &#8216;list&#8217;, &#8216;upload&#8217;, &#8216;get&#8217;</p>
<dl>
<dt>
</dt><dd> edit: Edit a document</dd>
<dt>
</dt><dd> Requires: title Optional: format, editor, folder</dd>
<dt>
</dt><dd> delete: Delete documents</dd>
<dt>
</dt><dd> Requires: none Optional: title</dd>
<dt>
</dt><dd> list: List documents</dd>
<dt>
</dt><dd> Requires: delimiter Optional: title, folder</dd>
<dt>
</dt><dd> upload: Upload a document</dd>
<dt>
</dt><dd> Requires: none Optional: title, folder, format Arguments: PATH_TO_FILE</dd>
<dt>
</dt><dd> get: Download a document</dd>
<dt>
</dt><dd> Requires: (title OR folder) Optional: format Arguments: LOCATION</dd></dl>
<p> Available tasks for service contacts: &#8216;list&#8217;, &#8216;list-groups&#8217;, &#8216;add&#8217;, &#8216;add-groups&#8217;, &#8216;delete-groups&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
</dt><dd> list: List contacts</dd>
<dt>
</dt><dd> Requires: none Arguments: Fields to show (example: name,email)</dd>
<dt>
</dt><dd> list-groups: List contact groups</dd>
<dt>
</dt><dd> Requires: none Arguments: Specific groups to list (if any)</dd>
<dt>
</dt><dd> add: Add contacts</dd>
<dt>
</dt><dd> Requires: none Arguments: &quot;name,email&quot; pair or CSV filename</dd>
<dt>
</dt><dd> add-groups: Add contact group(s)</dd>
<dt>
</dt><dd> Requires: none Arguments: Group name(s)</dd>
<dt>
</dt><dd> delete-groups: Delete contact group(s)</dd>
<dt>
</dt><dd> Requires: none Arguments: Group name(s)</dd>
<dt>
</dt><dd> delete: Delete contacts</dd>
<dt>
</dt><dd> Requires: none Arguments: names of contact(s) to delete (e.g. &quot;John Doe&quot; &quot;Jane Doe&quot;)</dd></dl>
<p> Available tasks for service calendar: &#8216;add&#8217;, &#8216;list&#8217;, &#8216;today&#8217;, &#8216;delete&#8217;</p>
<dl>
<dt>
</dt><dd> add: Add event to a calendar</dd>
<dt>
</dt><dd> Requires: none Optional: cal Arguments: QUICK_ADD_TEXT</dd>
<dt>
</dt><dd> list: List events on a calendar</dd>
<dt>
</dt><dd> Requires: delimiter Optional: title, query, date, cal</dd>
<dt>
</dt><dd> today: List events for the next 24 hours</dd>
<dt>
</dt><dd> Requires: delimiter Optional: title, query, cal</dd>
<dt>
</dt><dd> delete: Delete event from a calendar</dd>
<dt>
</dt><dd> Requires: (title OR query) Optional: date, cal</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>&#8211;blog</code>=<i>BLOG</i></dt>
<dd> Blogger only &#8211; specify a blog other than your primary.</dd>
<dt><code>&#8211;cal</code>=<i>CAL</i></dt>
<dd> Calendar only &#8211; specify a calendar other than your primary.</dd>
<dt><code>-c</code> CATEGORY, <code>&#8211;category</code>=<i>CATEGORY</i></dt>
<dd> YouTube only &#8211; specify video categories as a commaseparated list, e.g. &quot;Film, Travel&quot;</dd>
<dt><code>&#8211;config</code>=<i>CONFIG</i></dt>
<dd> Specify location of config file.</dd>
<dt><code>&#8211;devtags</code>=<i>DEVTAGS</i></dt>
<dd> YouTube only &#8211; specify developer tags as a commaseparated list.</dd>
<dt><code>&#8211;devkey</code>=<i>DEVKEY</i></dt>
<dd> YouTube only &#8211; specify a developer key</dd>
<dt><code>-d</code> DATE, <code>&#8211;date</code>=<i>DATE</i></dt>
<dd> Date in YYYY-MM-DD format. Picasa only &#8211; sets the date of the album Calendar only &#8211; date of the event to add / look for. Can also specify a range with a comma: &quot;YYYY-MM-DD&quot;, events between date and future. &quot;YYYYMM-DD,YYYY-MM-DD&quot; events between two dates.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Enable all debugging output, including HTTP data</dd>
<dt><code>&#8211;delimiter</code>=<i>DELIMITER</i></dt>
<dd> Specify a delimiter for the output of the list task.</dd>
<dt><code>&#8211;draft</code></dt>
<dd> Blogger only &#8211; post as a draft</dd>
<dt><code>&#8211;editor</code>=<i>EDITOR</i></dt>
<dd> Docs only &#8211; editor to use on a file.</dd>
<dt><code>-f</code> FOLDER, <code>&#8211;folder</code>=<i>FOLDER</i></dt>
<dd> Docs only &#8211; specify folder(s) to upload to / search in.</dd>
<dt><code>&#8211;format</code>=<i>FORMAT</i></dt>
<dd> Docs only &#8211; format to download documents as.</dd>
<dt><code>&#8211;hostid</code>=<i>HOSTID</i></dt>
<dd> Label the machine being used.</dd>
<dt><code>-n</code> TITLE, <code>&#8211;title</code>=<i>TITLE</i></dt>
<dd> Title of the item</dd>
<dt><code>&#8211;no-convert</code></dt>
<dd> Google Apps Premier only &#8211; do not convert the file on upload. (Else converts to native Google Docs format)</dd>
<dt><code>-o</code> OWNER, <code>&#8211;owner</code>=<i>OWNER</i></dt>
<dd> Username or ID of the owner of the resource. For example, &#8216;picasa list-albums <code>-o</code> bob&#8217; to list bob&#8217;s albums</dd>
<dt><code>-q</code> QUERY, <code>&#8211;query</code>=<i>QUERY</i></dt>
<dd> Full text query string for specifying items. Searches on titles, captions, and tags.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> Print only prompts and error messages</dd>
<dt><code>&#8211;reminder</code>=<i>REMINDER</i></dt>
<dd> Calendar only &#8211; specify time for added event&#8217;s reminder, e.g. &quot;10m&quot;, &quot;3h&quot;, &quot;1d&quot;</dd>
<dt><code>-s</code> SUMMARY, <code>&#8211;summary</code>=<i>SUMMARY</i></dt>
<dd> Description of the upload, or file containing the description.</dd>
<dt><code>-t</code> TAGS, <code>&#8211;tags</code>=<i>TAGS</i></dt>
<dd> Tags for item, e.g. &quot;Sunsets, Earth Day&quot;</dd>
<dt><code>-u</code> USER, <code>&#8211;user</code>=<i>USER</i></dt>
<dd> Username to log in with for the service.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Print all messages.</dd></dl>
<h2>EXAMPLES</h2>
<pre><code>
google blogger post-- title 'foo' 'command line posting' google calendar add 'Lunch with Jim at noon tomorrow' google contacts list name, email &gt; contacts.csv
                                                                                                                                                          google docs edit-- title 'Shopping list' google.py picasa create-- title 'Cat Photos' ~ /
                                                                                                                                                      photos / cats/*.jpg
google youtube post --category Education killer_robots.avi
</code></pre>
