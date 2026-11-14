---
title: "libfwup-h(3)"
name: "libfwup-h"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libfwup-h/"
description: "libfwup – library to support management of system firmware updates"
---

<p>libfwup &#8211; library to support management of system firmware updates</p>
<h2>Synopsis</h2>
<pre>#include &lt;<code>fwup.h</code>&gt;
<code>int </code>fwup_supported<code>(void);</code><br>
 - test if firmware updating is supported on the running machine
<code>typedef struct fwup_resource_s </code>fwup_resource<code>;</code><br>
<code>typedef struct fwup_resource_iter_s </code>fwup_resource_iter<code>;</code><br>
<code>int </code>fwup_resource_iter_create<code>(fwup_resource_iter **</code><i>iter</i><code>);</code><br>
<code>int </code>fwup_resource_iter_next<code>(fwup_resource_iter *</code><i>iter</i><code>,
fwup_resource **</code><i>re</i><code>);</code><br>
<code>int </code>fwup_resource_iter_destroy<code>(fwup_resource_iter **</code><i>iter</i><code>);</code><br>
 - iterate the list of updateable firmware images
<code>int </code>fwup_set_guid<code>(fwup_resource_iter *</code><i>iter</i><code>, fwup_resource **</code><i>re</i><code>,
const efi_guid_t *</code><i>guid</i><code>);</code><br>
 - manually set a guid for update
<code>int </code>fwup_set_guid_forced<code>(fwup_resource_iter *</code><i>iter</i><code>, fwup_resource **</code><i>re</i><code>,
const efi_guid_t *</code><i>guid</i><code>, bool </code><i>force</i><code>);</code><br>
 - manually set a guid for update (with a force option)
<code>void </code>fwup_resource_free<code>(fwup_resource *</code><i>re</i><code>);</code><br>
 - free resource allocated by fwup_set_guid_forced<code>()</code>
<code>int </code>fwup_set_up_update<code>(fwup_resource *</code><i>re</i><code>, uint64_t </code><i>hw_inst</i><code>, int </code><i>infd</i><code>);</code><br>
<code>int </code>fwup_clear_status<code>(fwup_resource *</code><i>re</i><code>);</code><br>
<code>int </code>fwup_get_guid<code>(fwup_resource *</code><i>re</i><code>, efi_guid_t **</code><i>guid</i><code>);</code><br>
<code>int </code>fwup_get_fw_version<code>(fwup_resource *</code><i>re</i><code>, uint32_t *</code><i>version</i><code>);</code><br>
<code>int </code>fwup_get_fw_type<code>(fwup_resource *</code><i>re</i><code>, uint32_t *</code><i>type</i><code>);</code><br>
<code>int </code>fwup_get_lowest_supported_fw_version<code>(fwup_resource *</code><i>re</i><code>,
uint32_t *</code><i>version</i><code>);</code><br>
<code>int </code>fwup_get_last_attempt_info<code>(fwup_resource *</code><i>re</i><code>, uint32_t *</code><i>version</i><code>,
uint32_t *</code><i>status</i><code>, time_t *</code><i>when</i><code>);</code><br>
 - operate on an individual firmware entry
<code>int </code>fwup_get_debug_log<code>(char **</code><i>utf8</i><code>, size_t *</code><i>size</i><code>);</code><br>
 - show the debug log from the last update attempt
<code>void </code>fwup_use_existing_media_path<code>(int </code><i>use_existing_media_path</i><code>);</code><br>
 - instruct fwupdate on whether to reuse old capsule filenames on the ESP.
<code>void </code>fwup_set_esp_mountpoint<code>(char *</code><i>path</i><code>);</code><br>
 - Override detection of the mountpoint for the ESP directory
<code>const char *</code>fwup_get_esp_mountpoint<code>(void);</code><br>
 - Get the current mountpoint for the ESP directory
<code>int </code>fwup_get_ux_capsule_info<code>(uint32_t *</code><i>screen_x_size</i><code>,
uint32_t *</code><i>screen_y_size</i><code>);</code><br>
 - get the dimensions of the screen during boot</pre>
<h2>Description</h2>
<pre><code>int </code>fwup_supported<code>(void);</code>
Tests if the current machine supports firmware updates
<code>typedef struct fwup_resource_s </code>fwup_resource<code>;</code><br>
<code>typedef struct fwup_resource_iter_s </code>fwup_resource_iter<code>;</code><br>
<code>int </code>fwup_resource_iter_create<code>(fwup_resource_iter **</code><i>iter</i><code>);</code><br>
Create a new firmware resoure iterator <i>iter</i>.
<code>int </code>fwup_resource_iter_next<code>(fwup_resource_iter *</code><i>iter</i><code>,
fwup_resource **</code><i>re</i><code>);</code><br>
Get the next firmware resource <i>re</i> from iterator <i>iter</i>.
<code>int </code>fwup_resource_iter_destroy<code>(fwup_resource_iter **</code><i>iter</i><code>);</code><br>
Destroy firmware resource iterator <i>iter</i>.
<code>int </code>fwup_set_up_update<code>(fwup_resource *</code><i>re</i><code>, uint64_t </code><i>hw_inst</i><code>, int </code><i>infd</i><code>);</code><br>
Set up an update for resource <i>re</i>, hardware instance number <i>hw_inst</i>,
with the file referenced by the file descriptor <i>infd</i>. <i>infd</i> must
support <a href="//www.systutorials.com/docs/linux/man/3-read/">read</a><code>(3)</code>.
<code>int </code>fwup_clear_status<code>(fwup_resource *</code><i>re</i><code>);</code><br>
Clear the status of the firmware resource <i>re</i>. This removes any pending
attempt to update it, as well as clearing any pending error report.
<code>int </code>fwup_get_guid<code>(fwup_resource *</code><i>re</i><code>, efi_guid_t **</code><i>guid</i><code>);</code><br>
Set <i>guid</i> to the GUID which uniquely identifies firmware resource <i>re</i>.
<code>int </code>fwup_get_fw_version<code>(fwup_resource *</code><i>re</i><code>, uint32_t *</code><i>version</i><code>);</code><br>
Set <i>version</i> to the version of the firmware resource <i>re</i>.
#define <code>FWUP_RESOURCE_TYPE_UNKNOWN</code> 0
#define <code>FWUP_RESOURCE_TYPE_SYSTEM_FIRMWARE</code> 1
#define <code>FWUP_RESOURCE_TYPE_DEVICE_FIRMWARE</code> 2
#define <code>FWUP_RESOURCE_TYPE_UEFI_DRIVER</code> 3
<code>int </code>fwup_get_fw_type<code>(fwup_resource *</code><i>re</i><code>, uint32_t *</code><i>type</i><code>);</code><br>
Set <i>type</i> to the type of the firmware resource <i>re</i>.
<code>int </code>fwup_get_lowest_supported_fw_version<code>(fwup_resource *</code><i>re</i><code>,
uint32_t *</code><i>version</i><code>);</code>
Set <i>version</i> to the lowest firmware version resource <i>re</i> can be
updated to.
<code>int </code>fwup_get_last_attempt_info<code>(fwup_resource *</code><i>re</i><code>, uint32_t *</code><i>version</i><code>,
uint32_t *</code><i>status</i><code>, time_t *</code><i>when</i><code>);</code><br>
Get the status for the last attempt to update firmware resource <i>re</i>.
<code>int </code>fwup_get_debug_log<code>(char **</code><i>utf8</i><code>, size_t *</code><i>size</i><code>);</code><br>
Get the debug log from the last update attempt. This allocates a buffer
which the caller must free.
<code>void </code>fwup_print_update_info<code>(void);</code><br>
Print the information of firmware update status.
<code>void </code>fwup_use_existing_media_path<code>(int </code><i>use_existing_media_path</i><code>);</code><br>
Instruct fwupdate on whether to reuse old capsule filenames on the ESP.
<code>void </code>fwup_set_esp_mountpoint<code>(char *</code><i>path</i><code>);</code><br>
Override detection of the mountpoint for the ESP directory.
<code>int </code>fwup_get_ux_capsule_info<code>(uint32_t *</code><i>screen_x_size</i><code>,
uint32_t *</code><i>screen_y_size</i><code>);</code><br>
Get the dimensions of the screen during boot.</pre>
<h2>Authors</h2>
<pre>Peter Jones &lt;pjones [at] redhat.com&gt;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3), <code><a href="/docs/linux/man/3-strerror_r/">strerror_r</a></code>(3)</p>
