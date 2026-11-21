---
title: "colormgr(1)"
name: "colormgr"
section: "1"
letter: "c"
url: "/docs/linux/man/1-colormgr/"
description: "colormgr – Color Manager Testing Tool"
---

<h2 class="name">NAME</h2>
<p> colormgr &#8211; Color Manager Testing Tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>colormgr</code> [<code>&#8211;verbose</code>] [<code>&#8211;version</code>]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>colormgr</code> command. </dd>
<p> <code>colormgr</code> allows an administrator to view and change color profile to device mappings.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (&#8216;-&#8216;). A summary of options is included below. </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show summary of options.</dd></dl>
<h2>COMMANDS</h2>
<p> This program takes commands with a variable number of arguments. </p>
<p> <code>create-device</code> <i>device_id</i> <i>scope</i></p>
<dl>
<dt>
</dt><dd> Create a device</dd></dl>
<p> <code>create-profile</code> <i>profile_id</i> <i>scope</i></p>
<dl>
<dt>
</dt><dd> Create a profile</dd></dl>
<p> <code>delete-device</code> <i>device</i></p>
<dl>
<dt>
</dt><dd> Deletes a device</dd></dl>
<p> <code>delete-profile</code> <i>profile</i></p>
<dl>
<dt>
</dt><dd> Deletes a profile</dd></dl>
<p> <code>device-add-profile</code> <i>device</i> <i>profile</i></p>
<dl>
<dt>
</dt><dd> Add a profile to a device that already exists</dd></dl>
<p> <code>device-get-default-profile</code> <i>device</i></p>
<dl>
<dt>
</dt><dd> Gets the default profile for a device</dd></dl>
<p> <code>device-get-profile-for-qualifier</code> <i>device</i> <i>qualifier</i></p>
<dl>
<dt>
</dt><dd> Returns all the profiles that match a qualifier</dd></dl>
<p> <code>device-inhibit</code> <i>device</i> <i>timeout</i></p>
<dl>
<dt>
</dt><dd> Inhibits colour profiles for this device</dd></dl>
<p> <code>device-make-profile-default</code> <i>device</i> <i>profile</i></p>
<dl>
<dt>
</dt><dd> Makes a profile default for a device</dd></dl>
<p> <code>device-set-enabled</code></p>
<dl>
<dt>
</dt><dd> Enables or disables the device</dd></dl>
<p> <code>device-set-kind</code> <i>device</i> <i>kind</i></p>
<dl>
<dt>
</dt><dd> Sets the device kind</dd></dl>
<p> <code>device-set-model</code> <i>device</i> <i>model</i></p>
<dl>
<dt>
</dt><dd> Sets the device model</dd></dl>
<p> <code>device-set-serial</code> <i>device</i> <i>serial</i></p>
<dl>
<dt>
</dt><dd> Sets the device serial</dd></dl>
<p> <code>device-set-vendor</code> <i>device</i> <i>vendor</i></p>
<dl>
<dt>
</dt><dd> Sets the device vendor</dd></dl>
<p> <code>find-device</code> <i>device_id</i></p>
<dl>
<dt>
</dt><dd> Find a device from the device ID</dd></dl>
<p> <code>find-device-by-property</code> <i>key</i> <i>value</i></p>
<dl>
<dt>
</dt><dd> Find a device with a given property value</dd></dl>
<p> <code>find-profile</code> <i>profile_id</i></p>
<dl>
<dt>
</dt><dd> Find a profile from the profile ID</dd></dl>
<p> <code>find-profile-by-filename</code> <i>filename</i></p>
<dl>
<dt>
</dt><dd> Find a profile by filename</dd></dl>
<p> <code>get-devices</code></p>
<dl>
<dt>
</dt><dd> Gets all the color managed devices</dd></dl>
<p> <code>get-devices-by-kind</code> <i>kind</i></p>
<dl>
<dt>
</dt><dd> Gets all the color managed devices of a specific kind</dd></dl>
<p> <code>get-profiles</code></p>
<dl>
<dt>
</dt><dd> Gets all the available color profiles</dd></dl>
<p> <code>get-sensor-reading</code> <i>display_type</i></p>
<dl>
<dt>
</dt><dd> Gets a reading from a sensor</dd></dl>
<p> <code>get-sensors</code></p>
<dl>
<dt>
</dt><dd> Gets all the available colour sensors</dd></dl>
<p> <code>get-standard-space</code> <i>standard_space</i></p>
<dl>
<dt>
</dt><dd> Get a standard colourspace</dd></dl>
<p> <code>import-profile</code> <i>filename</i></p>
<dl>
<dt>
</dt><dd> Copies an .icc file into the correct per-user directory and shows information about the imported profile.</dd></dl>
<p> <code>profile-set-property</code> <i>profile</i> <i>name</i> <i>value</i></p>
<dl>
<dt>
</dt><dd> Sets extra properties on the profile</dd></dl>
<p> <code>sensor-lock</code></p>
<dl>
<dt>
</dt><dd> Locks the colour sensor</dd></dl>
<p> <code>sensor-set-options</code> <i>name</i> <i>value</i></p>
<dl>
<dt>
</dt><dd> Sets one or more sensor options</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Richard Hughes &lt;richard [at] hughsie.com&gt;. </p>
