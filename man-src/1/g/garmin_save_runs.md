---
title: "garmin_save_runs(1)"
name: "garmin_save_runs"
section: "1"
letter: "g"
url: "/docs/linux/man/1-garmin_save_runs/"
description: "garmin_save_runs – retrieve track logs from a Forerunner device."
---

<h2>NAME</h2>
<p> garmin_save_runs &#8211; retrieve track logs from a Forerunner device.</p>
<h2>SYNOPSIS</h2>
<p> <code>garmin_save_runs</code> </p>
<p> <code>garmin_save_runs</code> retrieves track logs from a Garmin Forerunner device connected to an USB port, and saves the information into files. Files are saved with the extension &quot;.gmn&quot; and are named by the run start time (e.g. &#8216;20070121T151814.gmn&#8217;). The .gmn file format is a binary file format that can be unpacked with he <code>garmin_dump</code> or <code>garmin_gmap</code> utilities. It is substantially more efficient than the bloated XML format that Garmin uses. </p>
<p> The output of garmin_save_runs will tell you where on your filesystem the actual .gmn files were saved. The default is to save them in a directory tree (by year and month) under the current directory. You can override this by setting the environment variable GARMIN_SAVE_RUNS to whatever directory you like. Existing files are not overwritten. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-garmin_get_info/">garmin_get_info</a></code>(1), <code><a href="/docs/linux/man/1-garmin_dump/">garmin_dump</a></code>(1), <code><a href="/docs/linux/man/1-garmin_gmap/">garmin_gmap</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> garmin_save_runs was written by Dave Bailey. </p>
<h2>Index</h2>
