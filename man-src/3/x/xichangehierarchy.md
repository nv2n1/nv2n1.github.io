---
title: "xichangehierarchy(3)"
name: "xichangehierarchy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xichangehierarchy/"
---

XIChangeHierarchy - change the device hierarchy. 

<h2>Synopsis</h2><pre>#include &lt;X11/extensions/XInput2.h&gt;</pre><pre>Status XIChangeHierarchy( Display *display,
 XIAnyHierarchyChangeInfo *changes,
 int num_changes);</pre><pre>display
 Specifies the connection to the X server.</pre><pre>num_changes
 Specifies the number of elements in changes.</pre><pre>changes
 Specifies the changes to be made.</pre><h2>Description</h2><dl COMPACT><dd><pre>XIChangeHierarchy modifies the device hierarchy by creating or
removing master devices or changing the attachment of slave
devices. If num_changes is non-zero, changes is an array of
XIAnyHierarchyChangeInfo structures. If num_changes is equal or less than
zero, XIChangeHierarchy does nothing.</pre></dl><dl COMPACT><dd><pre>XIChangeHierarchy processes changes in order, effective
immediately. If an error occurs, processing is aborted and the
error is reported to the client. Changes already made remain
effective.</pre></dl><dl COMPACT><dd><pre>The list of changes is any combination of
XIAnyHierarchyChangeInfo. The type of a hierarchy change can be
XIAddMaster, XIRemoveMaster, XIAttachSlave or XIDetachSlave.</pre></dl><dl COMPACT><dd><pre>typedef union {
 int type;
 XIAddMasterInfo add;
 XIRemoveMasterInfo remove;
 XIAttachSlave attach;
 XIDetachSlave detach;
} XIAnyHierarchyChangeInfo;</pre></dl><dl COMPACT><dd><pre>typedef struct {
 int type; /* XIAddMaster */
 char* name;
 Bool send_core;
 Bool enable;
} XIAddMasterInfo;</pre></dl><dl COMPACT><dd><pre>typedef struct {
 int type; /* XIRemoveMaster */
 int deviceid;
 int return_mode;
 int return_pointer;
 int return_keyboard;
} XIRemoveMasterInfo;</pre></dl><dl COMPACT><dd><pre>typedef struct {
 int type; /* XIAttachSlave */
 int deviceid;
 int new_master;
} XIAttachSlaveInfo;</pre></dl><dl COMPACT><dd><pre>typedef struct {
 int type; /* XIDetachSlave */
 int deviceid;
} XIDetachSlaveInfo;</pre></dl><dl COMPACT><dd><pre>XIAddMasterInfo creates a new master pointer and a new
master keyboard labelled &quot;name pointer&quot; and &quot;name keyboard&quot;
respectively. If sendCore is True, the devices will send core
events. If enable is True, the device is enabled immediately.</pre></dl><dl COMPACT><dd><pre>XIAddMasterInfo can generate a BadValue error.</pre></dl><dl COMPACT><dd><pre>XIRemoveMasterInfo removes device and its paired master device.
If returnMode is XIAttachToMaster, all pointers attached to
device or its paired master device are attached to
returnPointer. Likewise, all keyboards are attached to
returnKeyboard. If returnMode is XIFloating, all attached
devices are set to floating.</pre></dl><dl COMPACT><dd><pre>XIRemoveMasterInfo can generate a BadValue and a BadDevice
error.</pre></dl><dl COMPACT><dd><pre>XIAttachSlaveInfo attaches device to new_master. If the device
is currently attached to a master device, it is detached from
the master device and attached to the new master device.</pre></dl><dl COMPACT><dd><pre>XIAttachSlaveInfo can generate a BadDevice error.</pre></dl><dl COMPACT><dd><pre>XIDettachSlaveInfo deattaches device from the current master
device and sets it floating. If the device is already floating,
no changes are made.</pre></dl><dl COMPACT><dd><pre>XIDetachSlaveInfo can generate a BadDevice error.</pre></dl><dl COMPACT><dd><pre>XIChangeHierarchy generates an XIHierarchyEvent if any
modifications were successful.</pre></dl><h2>Diagnostics</h2><dl COMPACT><dd><pre>BadDevice
 An invalid device was specified. The device does not
 exist or is not a appropriate for the type of change.</pre></dl><dl COMPACT><dd><pre>BadValue
 Some numeric value falls out of the allowed range.</pre></dl>
