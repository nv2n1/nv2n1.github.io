---
title: "efi_del_variable(3)"
name: "efi_del_variable"
section: "3"
letter: "e"
url: "/docs/linux/man/3-efi_del_variable/"
description: "efi_variables_supported, efi_del_variable, efi_get_variable, efi_get_variable_attributes, efi_get_variable_size, efi_set_variable – manipulate UEFI variables"
---

<h2>NAME</h2>
<p> efi_variables_supported, efi_del_variable, efi_get_variable, efi_get_variable_attributes, efi_get_variable_size, efi_set_variable &#8211; manipulate UEFI variables</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;efivar.h&gt;
int efi_variables_supported(void);
int efi_del_variable(efi_guid_t guid, const char *name);
int efi_get_variable(efi_guid_t guid, const char *name,
                     void **data, ssize_t *data_size,
                     uint32_t *attributes);
int efi_get_variable_attributes(efi_guid_t guid, const char *name,
                                uint32_t *attributes);
int efi_get_variable_size(efi_guid_t guid, const char *name,
                          size_t *size);
int efi_append_variable(efi_guid_t guid, const char *name,
                        void *data, size_t data_size,
                        uint32_t attributes);
int efi_set_variable(efi_guid_t guid, const char *name,
                     void *data, size_t data_size,
                     uint32_t attributes);
int efi_get_next_variable_name(efi_guid_t **guid, char **name);
int efi_str_to_guid(const char *s, efi_guid_t *guid);
int efi_guid_to_str(const efi_guid_t *guid, char **sp);
int efi_name_to_guid(const char *name, efi_guid_t *guid);
int efi_guid_to_name(efi_guid_t *guid, char **name);
int efi_guid_to_symbol(efi_guid_t *guid, char **symbol);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>efi_variables_supported</code>() tests if the UEFI variable facility is supported on the current machine. </p>
<p> <code>efi_del_variable</code>() deletes the variable specified by <i>guid</i> and <i>name</i>. </p>
<p> <code>efi_get_variable</code>() gets the variable specified by <i>guid</i> and <i>name</i>. The value is stored in <i>data</i>, its size in <i>data_size</i>, and its attributes are stored in <i>attributes</i>. </p>
<p> <code>efi_get_variable_attributes</code>() gets attributes for the variable specified by <i>guid</i> and <i>name</i>. </p>
<p> <code>efi_get_variable_size</code>() gets the size of the data for the variable specified by <i>guid</i> and <i>name</i>. </p>
<p> <code>efi_append_variable</code>() appends <i>data</i> of size <i>size</i> to the variable specified by <i>guid</i> and <i>name</i>. </p>
<p> <code>efi_set_variable</code>() sets the variable specified by <i>guid</i> and <i>name</i>. </p>
<p> <code>efi_get_next_variable_name</code>() iterates across the currently extant variables, passing back a guid and name. </p>
<p> <code>efi_str_to_guid</code>() parses a UEFI GUID from string form to an efi_guid_t the caller provides </p>
<p> <code>efi_guid_to_str</code>() allocates a suitable string and populates it with string representation of a UEFI GUID. It is the caller&#8217;s responsibility to free this string. </p>
<p> <code>efi_name_to_guid</code>() translates from a well known name to an efi_guid_t the caller provides. </p>
<p> <code>efi_guid_to_name</code>() translates from an efi_guid_t to a well known name. If the supplied GUID does not have a well known name, this function is equivalent to <code>efi_guid_to_str</code>(). </p>
<p> <code>efi_guid_to_symbol</code>() translates from an efi_guid_t to a unique (within libefivar) C-sytle symbol name. These symbol names are useful for printing as a unique, easily parsed identifier, and are also provide by the library and its header files. </p>
<h2>RETURN VALUE</h2>
<p> <code>efi_variables_supported</code>() returns true if variables are supported on the running hardware, and false if they are not. </p>
<p> <code>efi_get_next_variable_name</code>() returns 0 when iteration has completed, 1 when iteration has not completed, and -1 on error. In the event of an error, <i><a href="/docs/linux/man/3-errno/">errno</a></i>(3) is set appropriately. </p>
<p> <code>efi_del_variable</code>(), <code>efi_get_variable</code>(), <code>efi_get_variable_attributes</code>(), <code>efi_get_variable_size</code>(), <code>efi_append_variable</code>(), <code>efi_set_variable</code>(), <code>efi_str_to_guid</code>(), <code>efi_guid_to_str</code>(), <code>efi_name_to_guid</code>(), and <code>efi_guid_to_name</code>() return negative on error and zero on success.</p>
<h2>AUTHORS</h2>
<pre>
Peter Jones &lt;pjones [at] redhat.com&gt;
</pre>
<h2>Index</h2>
