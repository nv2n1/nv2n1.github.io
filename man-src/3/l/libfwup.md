---
title: "libfwup(3)"
name: "libfwup"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libfwup/"
description: "libfwup – library to support management of system firmware updates"
---

<h2>NAME</h2>
<p> libfwup &#8211; library to support management of system firmware updates</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fwup.h&gt;
int fwup_supported(void);
- test if firmware updating is supported on the running machine typedef struct fwup_resource_s fwup_resource;
typedef struct fwup_resource_iter_s fwup_resource_iter;
int fwup_resource_iter_create(fwup_resource_iter **iter);
int fwup_resource_iter_next(fwup_resource_iter *iter,
                            fwup_resource **re);
int fwup_resource_iter_destroy(fwup_resource_iter **iter);
- iterate the list of updateable firmware images int fwup_set_guid(fwup_resource_iter *iter, fwup_resource **re,
                                                                   const efi_guid_t *guid);
 - manually set a guid for update
int fwup_set_guid_forced(fwup_resource_iter *iter, fwup_resource **re,
const efi_guid_t *guid, bool force);
 - manually set a guid for update (with a force option)
void fwup_resource_free(fwup_resource *re);
 - free resource allocated by fwup_set_guid_forced()int fwup_set_up_update(fwup_resource *re, uint64_t hw_inst, int infd);
 int fwup_clear_status(fwup_resource *re);
 int fwup_get_guid(fwup_resource *re, efi_guid_t **guid);
 int fwup_get_fw_version(fwup_resource *re, uint32_t *version);
 int fwup_get_fw_type(fwup_resource *re, uint32_t *type);
 int fwup_get_lowest_supported_fw_version(fwup_resource *re,
                                          uint32_t *version);
 int fwup_get_last_attempt_info(fwup_resource *re, uint32_t *version,
                                uint32_t *status, time_t *when);
 - operate on an individual firmware entry int fwup_get_debug_log(char **utf8, size_t *size);
 - show the debug log from the last update attempt void fwup_use_existing_media_path(int use_existing_media_path);
 - instruct fwupdate on whether to reuse old capsule filenames on the ESP.void fwup_set_esp_mountpoint(char *path);
 - Override detection of the mountpoint for the ESP directory
const char *fwup_get_esp_mountpoint(void);
 - Get the current mountpoint for the ESP directory
int fwup_get_ux_capsule_info(uint32_t *screen_x_size,
uint32_t *screen_y_size);
 - get the dimensions of the screen during boot
</code></pre>
<h2>DESCRIPTION</h2>
<pre><code>
int fwup_supported(void);
Tests if the current machine supports firmware updates typedef struct fwup_resource_s fwup_resource;
typedef struct fwup_resource_iter_s fwup_resource_iter;
int fwup_resource_iter_create(fwup_resource_iter **iter);
Create a new firmware resoure iterator iter.int fwup_resource_iter_next(fwup_resource_iter *iter,
                                                                        fwup_resource **re);
Get the next firmware resource re from iterator iter.int fwup_resource_iter_destroy(fwup_resource_iter **iter);
Destroy firmware resource iterator iter.int fwup_set_up_update(fwup_resource *re, uint64_t hw_inst, int infd);
Set up an update for resource re, hardware instance number hw_inst,
with the file referenced by the file descriptor infd.  infd must
support read(3).
int fwup_clear_status(fwup_resource *re);
Clear the status of the firmware resource re.This removes any pending
    attempt to update it,
    as well as clearing any pending error report.int fwup_get_guid(fwup_resource *re, efi_guid_t **guid);
Set guid to the GUID which uniquely identifies firmware resource re.int fwup_get_fw_version(fwup_resource *re, uint32_t *version);
Set version to the version of the firmware resource re.
#define FWUP_RESOURCE_TYPE_UNKNOWN 0
#define FWUP_RESOURCE_TYPE_SYSTEM_FIRMWARE 1
#define FWUP_RESOURCE_TYPE_DEVICE_FIRMWARE 2
#define FWUP_RESOURCE_TYPE_UEFI_DRIVER 3
    int
    fwup_get_fw_type(fwup_resource *re, uint32_t *type);
Set type to the type of the firmware resource re.int fwup_get_lowest_supported_fw_version(fwup_resource *re,
                                                                                          uint32_t *version);
Set version to the lowest firmware version resource re can be
    updated to.int
    fwup_get_last_attempt_info(fwup_resource *re, uint32_t *version,
                               uint32_t *status, time_t *when);
Get the status for the last attempt to update firmware resource re.
int fwup_get_debug_log(char **utf8, size_t *size);
Get the debug log from the last update attempt.This allocates a buffer
    which the caller must free.void
    fwup_print_update_info(void);
Print the information of firmware update status.void fwup_use_existing_media_path(int use_existing_media_path);
Instruct fwupdate on whether to reuse old capsule filenames on the ESP.void fwup_set_esp_mountpoint(char *path);
Override detection of the mountpoint for the ESP directory.
int fwup_get_ux_capsule_info(uint32_t *screen_x_size,
uint32_t *screen_y_size);
Get the dimensions of the screen during boot.
</code></pre>
<h2>AUTHORS</h2>
<pre>
Peter Jones &lt;pjones [at] redhat.com&gt;
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3), <code><a href="/docs/linux/man/3-strerror_r/">strerror_r</a></code>(3) </p>
<h2>Index</h2>
