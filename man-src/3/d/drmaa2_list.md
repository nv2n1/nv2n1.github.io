---
title: "drmaa2_list(3)"
name: "drmaa2_list"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa2_list/"
description: "– DRMAA2 list routines"
---

<h2 class="name">NAME</h2>
<p>&nbsp;&#8211; DRMAA2 list routines </p>
<h2>SYNOPSIS</h2>
<p> <code>#include drmaa.h</code> </p>
<pre><code>
struct drmaa2_list_s; /*forward*/
typedef struct drmaa2_list_s *drmaa2_list;
typedef struct drmaa2_list_s *drmaa2_string_list;
typedef struct drmaa2_list_s *drmaa2_j_list;
typedef struct drmaa2_list_s *drmaa2_queueinfo_list;
typedef struct drmaa2_list_s *drmaa2_machineinfo_list;
typedef struct drmaa2_list_s *drmaa2_slotinfo_list;
typedef struct drmaa2_list_s *drmaa2_r_list;
typedef enum drmaa2_listtype {
    DRMAA2_STRINGLIST,
    DRMAA2_JOBLIST,
    DRMAA2_QUEUEINFOLIST,
    DRMAA2_MACHINEINFOLIST,
    DRMAA2_SLOTINFOLIST,
    DRMAA2_RESERVATIONLIST
} drmaa2_listtype;
typedef void (*drmaa2_list_entryfree)(void **value);
drmaa2_list drmaa2_list_create(const drmaa2_listtype t, const drmaa2_list_entryfree callback);
void drmaa2_list_free(drmaa2_list *l);
const void *drmaa2_list_get(const drmaa2_list l, long pos);
drmaa2_error drmaa2_list_add(drmaa2_list l, const void *value);
drmaa2_error drmaa2_list_del(drmaa2_list l, long pos);
long drmaa2_list_size(const drmaa2_list l);
</code></pre>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>drmaa2_list_create</code>()</p>
<dd> Creates a new list instance for the specified type of items. Returns a pointer to the list or NULL on error. Optional parameter <i>callback</i> allows the application to provide a callback pointer to a collection element cleanup function. <code>DRMAA2_UNSET_CALLBACK</code> may be supplied instead of a valid callback pointer.</p>
<dt><code>drmaa2_list_free</code>()</p>
<dd> Frees the list and the contained members. If a callback function was provided on list creation, it SHALL be called once per list item.</p>
<dt><code>drmaa2_list_get</code>()</p>
<dd> Gets the list element at the indicated position. The element index starts at zero. If the index is invalid, the function returns NULL.</p>
<dt><code>drmaa2_list_add</code>()</p>
<dd> Adds a new item at the end of the list and returns a success indication. The list MUST contain only the provided pointer, not a deep copy of the provided data structure.</p>
<dt><code>drmaa2_list_del</code>()</p>
<dd> Removes the list element at the indicated position and returns a success indication. If a callback function was provided on list creation, it SHALL be called before this function returns.</p>
<dt><code>drmaa2_list_size</code>()</p>
<dd> Returns the number of elements in the list. If the list is empty, then the function returns 0, which SHALL NOT be treated as an error case.</dl>
<h2>SEE ALSO</h2>
<h2>Index</h2>
