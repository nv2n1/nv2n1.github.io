---
title: "defined(3)"
name: "defined"
section: "3"
letter: "d"
url: "/docs/linux/man/3-defined/"
---

<h2 class="name">NAME</h2>
 

 

 libmaxminddb - a library for working with MaxMind DB files 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &amp;nbsp; &lt; maxminddb.h&gt;
int MMDB_open(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const char &amp;nbsp; *const filename,
                                                  &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; uint32_t flags,
                         &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb);
void MMDB_close(MMDB_s &amp;nbsp; *const mmdb);
MMDB_lookup_result_s MMDB_lookup_string(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb,
                                               &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; const char &amp;nbsp; *const ipstr,
                                           &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; int &amp;nbsp; *const gai_error,
                                    &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; int &amp;nbsp; *const mmdb_error);
MMDB_lookup_result_s MMDB_lookup_sockaddr(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb,
                                               &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; const struct sockaddr &amp;nbsp; *const
        &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; sockaddr,
                         &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; int &amp;nbsp; *const mmdb_error);
int MMDB_get_value(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_s &amp; nbsp; *const start,
                                                     &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_s &amp; nbsp; *const entry_data,
                                                   &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp;...);
int MMDB_vget_value(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_s &amp; nbsp; *const start,
                                                     &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_s &amp; nbsp; *const entry_data,
                                                   &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; va_list va_path);
int MMDB_aget_value(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_s &amp; nbsp; *const start,
                                                     &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_s &amp; nbsp; *const entry_data,
                                                   &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; const char &amp;nbsp; *const &amp;nbsp; *const path);
int MMDB_get_entry_data_list(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_s &amp; nbsp; *start,
                                                     &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_list_s &amp; nbsp; **const entry_data_list);
void MMDB_free_entry_data_list(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_list_s &amp; nbsp; *const entry_data_list);
int MMDB_get_metadata_as_entry_data_list(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb,
                                               &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_list_s &amp; nbsp; **const entry_data_list);
int MMDB_dump_entry_data_list(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; FILE &amp; nbsp; *const stream,
                                             &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_list_s &amp; nbsp; *const entry_data_list,
                                                        &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; int indent);
int MMDB_read_node(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb,
                                               &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; uint32_t node_number,
                         &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_search_node_s &amp; nbsp; *const node);
const char &amp;nbsp;
*MMDB_lib_version(void);
const char &amp;nbsp;
*MMDB_strerror(int error_code);
typedef struct MMDB_lookup_result_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    bool found_entry;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_entry_s entry;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint16_t netmask;
}
&amp;nbsp;
MMDB_lookup_result_s;
typedef struct MMDB_entry_data_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    bool has_data;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    union &amp;nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        uint32_t pointer;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        const char &amp;nbsp;
        *utf8_string;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        double double_value;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        const uint8_t &amp;nbsp;
        *bytes;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        uint16_t uint16;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        uint32_t uint32;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        int32_t int32;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        uint64_t uint64;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        {mmdb_uint128_t or uint8_t[16]} &amp; nbsp;
        uint128;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        bool boolean;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        float float_value;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    };
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    ...
        &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint32_t data_size;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint32_t type;
}
&amp;nbsp;
MMDB_entry_data_s;
typedef struct MMDB_entry_data_list_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_entry_data_s entry_data;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    struct MMDB_entry_data_list_s &amp;nbsp;
    *next;
}
&amp;nbsp;
MMDB_entry_data_list_s;
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 The libmaxminddb library provides functions for working MaxMind DB files. See <a rel="nofollow" HREF="http://maxmind.github.io/MaxMind-DB/">http://maxmind.github.io/MaxMind-DB/</a> for the MaxMind DB format specification. The database and results are all represented by different data structures. Databases are opened by calling MMDB_open(). You can look up IP addresses as a string with MMDB_lookup_string() or as a pointer to a sockaddr structure with MMDB_lookup_sockaddr(). 

 If the lookup finds the IP address in the database, it returns a MMDB_lookup_result_s structure. If that structure indicates that the database has data for the IP, there are a number of functions that can be used to fetch that data. These include MMDB_get_value() and MMDB_get_entry_data_list(). See the function documentation below for more details. 

 When you are done with the database handle you should call MMDB_close(). 

 All publicly visible functions, structures, and macros begin with &quot;MMDB_&quot;.

<h2>DATA STRUCTURES</h2>

 

 All data structures exported by this library's maxminddb.h header are typedef'd in the form typedef struct foo_s&nbsp;{&nbsp;...&nbsp;}&nbsp;foo_s so you can refer to them without the struct prefix. 

 This library provides the following data structures:

<h3>MMDB_s</h3>

 

 This is the handle for a MaxMind DB file. We only document some of this structure's fields intended for public use. All other fields are subject to change and are intended only for internal use.
<dl>
<dt>
<dd> 
typedef struct MMDB_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint32_t flags;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    const char &amp;nbsp;
    *filename;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    ...
        &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_metadata_s metadata;
}
&amp;nbsp;
MMDB_s;

<dt>&bull;
<dd> uint32_t flags - the flags this database was opened with. See the MMDB_open() documentation for more details.
<dt>&bull;
<dd> const char&nbsp;*filename - the name of the file which was opened, as passed to MMDB_open().
<dt>&bull;
<dd> MMDB_metadata_s metadata - the metadata for the database.</dl>

<h3>MMDB_metadata_s and MMDB_description_s</h3>

 

 This structure can be retrieved from the MMDB_s structure. It contains the metadata read from the database file. Note that you may find it more convenient to access this metadata by calling MMDB_get_metadata_as_entry_data_list() instead.
<dl>
<dt>
<dd> 
typedef struct MMDB_metadata_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint32_t node_count;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint16_t record_size;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint16_t ip_version;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    const char &amp;nbsp;
    *database_type;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    struct &amp;nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        size_t count;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        const char &amp;nbsp;
        **names;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    &amp;nbsp;
    languages;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint16_t binary_format_major_version;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint16_t binary_format_minor_version;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint64_t build_epoch;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    struct &amp;nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        size_t count;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        MMDB_description_s &amp;nbsp;
        **descriptions;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    &amp;nbsp;
    description;
}
&amp;nbsp;
MMDB_metadata_s;
typedef struct MMDB_description_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    const char &amp;nbsp;
    *language;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    const char &amp;nbsp;
    *description;
}
&amp;nbsp;
MMDB_description_s;
</dl>
 

 These structures should be mostly self-explanatory. 

 The ip_version member should always be 4 or 6. The binary_format_major_version should always be 2. 

 There is no requirement that the database metadata include languages or descriptions, so the count for these parts of the metadata can be zero. All of the other MMDB_metadata_s fields should be populated.

<h3>MMDB_lookup_result_s</h3>

 

 This structure is returned as the result of looking up an IP address.
<dl>
<dt>
<dd> 
typedef struct MMDB_lookup_result_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    bool found_entry;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_entry_s entry;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint16_t netmask;
}
&amp;nbsp;
MMDB_lookup_result_s;
</dl>
 

 If the found_entry member is false then the other members of this structure do not contain meaningful values. Always check that found_entry is true first. 

 The entry member is used to look up the data associated with the IP address. 

 The netmask member tells you what subnet the IP address belongs to in this database. For example, if you look up the address 1.1.1.1 in an IPv4 database and the returned netmask is 16, then the address is part of the 1.1.0.0/16 subnet. 

 If the database is an IPv6 database, the returned netmask is always an IPv6 prefix length (from 0-128), even if that database also contains IPv4 networks. If you look up an IPv4 address and would like to turn the netmask into an IPv4 netmask value, you can simply subtract 96 from the value.

<h3>MMDB_result_s</h3>

 

 You don't really need to dig around in this structure. You'll get this from a MMDB_lookup_result_s structure and pass it to various functions.

<h3>MMDB_entry_data_s</h3>

 

 This structure is used to return a single data section entry for an IP. These entries can in turn point to other entries, as is the case for things like maps and arrays. Some members of this structure are not documented as they are only for internal use.
<dl>
<dt>
<dd> 
typedef struct MMDB_entry_data_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    bool has_data;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    union &amp;nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        uint32_t pointer;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        const char &amp;nbsp;
        *utf8_string;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        double double_value;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        const uint8_t &amp;nbsp;
        *bytes;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        uint16_t uint16;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        uint32_t uint32;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        int32_t int32;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        uint64_t uint64;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        {mmdb_uint128_t or uint8_t[16]} &amp; nbsp;
        uint128;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        bool boolean;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        float float_value;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    };
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    ...
        &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint32_t data_size;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint32_t type;
}
&amp;nbsp;
MMDB_entry_data_s;
</dl>
 

 The has_data member is true if data was found for a given lookup. See MMDB_get_value() for more details. If this member is false then none of the other values in the structure are meaningful. 

 The union at the beginning of the structure defines the actual data. To determine which union member is populated you should look at the type member. The pointer member of the union should never be populated in any data returned by the API. Pointers should always be resolved internally. 

 The data_size member is only relevant for utf8_string and bytes data. utf8_string is not null terminated and data_size must be used to determine its length. 

 The type member can be compared to one of the MMDB_DTYPE_* macros.

<h3>128-bit Integers</h3>

 

 The handling of uint128 data depends on how your platform supports 128-bit integers, if it does so at all. With GCC 4.4 and 4.5 we can write unsigned int&nbsp;__attribute__&nbsp;((__mode__&nbsp;(TI))). With newer versions of GCC (4.6+) and clang (3.2+) we can simply write &quot;unsigned __int128&quot;. 

 In order to work around these differences, this library defines an mmdb_uint128_t type. This type is defined in the maxminddb.h header so you can use it in your own code. 

 With older compilers, we can't use an integer so we instead use a 16 byte array of uint8_t values. This is the raw data from the database. 

 This library provides a public macro MMDB_UINT128_IS_BYTE_ARRAY macro. If this is true (1), then uint128 values are returned as a byte array, if it is false then they are returned as a mmdb_uint128_t integer.

<h3>Data Type Macros</h3>

 

 This library provides a macro for every data type defined by the MaxMind DB spec.
<dl>
<dt>&bull;
<dd> MMDB_DATA_TYPE_UTF8_STRING
<dt>&bull;
<dd> MMDB_DATA_TYPE_DOUBLE
<dt>&bull;
<dd> MMDB_DATA_TYPE_BYTES
<dt>&bull;
<dd> MMDB_DATA_TYPE_UINT16
<dt>&bull;
<dd> MMDB_DATA_TYPE_UINT32
<dt>&bull;
<dd> MMDB_DATA_TYPE_MAP
<dt>&bull;
<dd> MMDB_DATA_TYPE_INT32
<dt>&bull;
<dd> MMDB_DATA_TYPE_UINT64
<dt>&bull;
<dd> MMDB_DATA_TYPE_UINT128
<dt>&bull;
<dd> MMDB_DATA_TYPE_ARRAY
<dt>&bull;
<dd> MMDB_DATA_TYPE_BOOLEAN
<dt>&bull;
<dd> MMDB_DATA_TYPE_FLOAT</dl>
 

 There are also a few types that are for internal use only:
<dl>
<dt>&bull;
<dd> MMDB_DATA_TYPE_EXTENDED
<dt>&bull;
<dd> MMDB_DATA_TYPE_POINTER
<dt>&bull;
<dd> MMDB_DATA_TYPE_CONTAINER
<dt>&bull;
<dd> MMDB_DATA_TYPE_END_MARKER</dl>
 

 If you see one of these in returned data then something has gone very wrong. The database is damaged or was generated incorrectly or there is a bug in the libmaxminddb code.

<h3>Pointer Values and MMDB_close()</h3>

 

 The utf8_string, bytes, and (maybe) the uint128 members of this structure are all pointers directly into the database's data section. This can either be a malloc'd or mmap'd block of memory. In either case, these pointers will become invalid after MMDB_close() is called. 

 If you need to refer to this data after that time you should copy the data with an appropriate function (strdup, memcpy, etc.).

<h3>MMDB_entry_data_list_s</h3>

 

 This structure encapsulates a linked list of MMDB_entry_data_s structures.
<dl>
<dt>
<dd> 
typedef struct MMDB_entry_data_list_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_entry_data_s entry_data;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    struct MMDB_entry_data_list_s &amp;nbsp;
    *next;
}
&amp;nbsp;
MMDB_entry_data_list_s;
</dl>
 

 This structure lets you look at entire map or array data entry by iterating over the linked list.

<h3>MMDB_search_node_s</h3>

 

 This structure encapsulates the two records in a search node. This is really only useful if you want to write code that iterates over the entire search tree as opposed to looking up a specific IP address.
<dl>
<dt>
<dd> 
typedef struct MMDB_search_node_s &amp;nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint64_t left_record;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint64_t right_record;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint8_t left_record_type;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    uint8_t right_record_type;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_entry_s left_record_entry;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_entry_s right_record_entry;
}
&amp;nbsp;
MMDB_search_node_s;
</dl>
 

 The two record types will take one of the following values:
<dl>
<dt>&bull;
<dd> MMDB_RECORD_TYPE_SEARCH_NODE - The record points to the next search node.
<dt>&bull;
<dd> MMDB_RECORD_TYPE_EMPTY - The record is a placeholder that indicates there is no data for the IP address. The search should end here.
<dt>&bull;
<dd> MMDB_RECORD_TYPE_DATA - The record is for data in the data section of the database. Use the entry for the record when looking up the data for the record.
<dt>&bull;
<dd> MMDB_RECORD_TYPE_INVALID - The record is invalid. Either an invalid node was looked up or the database is corrupt.</dl>
 

 The MMDB_entry_s for the record is only valid if the type is MMDB_RECORD_TYPE_DATA. Attempts to use an entry for other record types will result in an error or invalid data.

<h2>STATUS CODES</h2>

 

 This library returns (or populates) status codes for many functions. These status codes are:
<dl>
<dt>&bull;
<dd> MMDB_SUCCESS - everything worked
<dt>&bull;
<dd> MMDB_FILE_OPEN_ERROR - there was an error trying to open the MaxMind DB file.
<dt>&bull;
<dd> MMDB_IO_ERROR - an IO operation failed. Check errno for more details.
<dt>&bull;
<dd> MMDB_CORRUPT_SEARCH_TREE_ERROR - looking up an IP address in the search tree gave us an impossible result. The database is damaged or was generated incorrectly or there is a bug in the libmaxminddb code.
<dt>&bull;
<dd> MMDB_INVALID_METADATA_ERROR - something in the database is wrong. This includes missing metadata keys as well as impossible values (like an ip_version of 7).
<dt>&bull;
<dd> MMDB_UNKNOWN_DATABASE_FORMAT_ERROR - The database metadata indicates that it's major version is not 2. This library can only handle major version 2.
<dt>&bull;
<dd> MMDB_OUT_OF_MEMORY_ERROR - a memory allocation call (malloc, etc.) failed.
<dt>&bull;
<dd> MMDB_INVALID_DATA_ERROR - an entry in the data section contains invalid data. For example, a uint16 field is claiming to be more than 2 bytes long. The database is probably damaged or was generated incorrectly.
<dt>&bull;
<dd> MMDB_INVALID_LOOKUP_PATH_ERROR - The lookup path passed to MMDB_get_value, MMDB_vget_value, or MMDB_aget_value contains an array offset that is larger than LONG_MAX or smaller than LONG_MIN.
<dt>&bull;
<dd> MMDB_LOOKUP_PATH_DOES_NOT_MATCH_DATA_ERROR - The lookup path passed to MMDB_get_value,MMDB_vget_value, or MMDB_aget_value does not match the data structure for the entry. There are number of reasons this can happen. The lookup path could include a key not in a map. The lookup path could include an array index larger than an array or smaller than the minimum offset from the end of an array. It can also happen when the path expects to find a map or array where none exist.</dl>
 

 All status codes should be treated as int values.

<h3>MMDB_strerror()</h3>

<dl>
<dt>
<dd> 
const char &amp;nbsp;
*MMDB_strerror(int error_code)
</dl>
 

 This function takes a status code and returns an English string explaining the status.

<h2>FUNCTIONS</h2>

 

 This library provides the following exported functions:

<h3>MMDB_open()</h3>

<dl>
<dt>
<dd> 
int MMDB_open(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; const char &amp;nbsp; *const filename,
                                                  &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; uint32_t flags,
                         &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb);
</dl>
 

 This function opens a handle to a MaxMind DB file. Its return value is a status code as defined above. Always check this call's return value.
<dl>
<dt>
<dd> 
MMDB_s mmdb;
int status &amp;nbsp;
=
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_open("/path/to/file.mmdb", MMDB_MODE_MMAP, &amp;nbsp; &amp;mmdb);
if
    &amp;nbsp;
(MMDB_SUCCESS &amp;nbsp; != &amp;nbsp; status) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
... MMDB_close(&amp;mmdb);
</dl>
 

 filename must be encoded as UTF-8 on Windows. 

 The MMDB_s structure you pass in can be on the stack or allocated from the heap. However, if the open is successful it will contain heap-allocated data, so you need to close it with MMDB_close(). If the status returned is not MMDB_SUCCESS then this library makes sure that all allocated memory is freed before returning. 

 The flags currently provided are:
<dl>
<dt>&bull;
<dd> MMDB_MODE_MMAP - open the database with mmap().</dl>
 

 Passing in other values for flags may yield unpredictable results. In the future we may add additional flags that you can bitwise-or together with the mode, as well as additional modes. 

 You can also pass 0 as the flags value in which case the database will be opened with the default flags. However, these defaults may change in future releases. The current default is MMDB_MODE_MMAP.

<h3>MMDB_close()</h3>

<dl>
<dt>
<dd> 
void MMDB_close(MMDB_s &amp;nbsp; *const mmdb);
</dl>
 

 This frees any allocated or mmap'd memory that is held from the MMDB_s structure. It does not free the memory allocated for the structure itself! If you allocated the structure from the heap then you are responsible for freeing it.

<h3>MMDB_lookup_string()</h3>

<dl>
<dt>
<dd> 
MMDB_lookup_result_s MMDB_lookup_string(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb,
                                               &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; const char &amp;nbsp; *const ipstr,
                                           &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; int &amp;nbsp; *const gai_error,
                                    &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; int &amp;nbsp; *const mmdb_error);
</dl>
 

 This function looks up an IP address that is passed in as a null-terminated string. Internally it calls getaddrinfo() to resolve the address into a binary form. It then calls MMDB_lookup_sockaddr() to look the address up in the database. If you have already resolved an address you can call MMDB_lookup_sockaddr() directly, rather than resolving the address twice.
<dl>
<dt>
<dd> 
int gai_error, mmdb_error;
MMDB_lookup_result_s result &amp;nbsp;
=
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_lookup_string(&amp;mmdb, &amp;nbsp; "1.2.3.4", &amp;nbsp; &amp;gai_error, &amp;nbsp; &amp;mmdb_error);
if
    &amp;nbsp;
(0 &amp; nbsp; != &amp;nbsp; gai_error) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
if
    &amp;nbsp;
(MMDB_SUCCESS &amp;nbsp; != &amp;nbsp; mmdb_error) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
if
    &amp;nbsp;
(result.found_entry) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
</dl>
 

 This function always returns an MMDB_lookup_result_s structure, but you should also check the gai_error and mmdb_error parameters. If either of these indicates an error then the returned structure is meaningless. 

 If no error occurred you still need to make sure that the found_entry member in the returned result is true. If it's not, this means that the IP address does not have an entry in the database. 

 This function will work with IPv4 addresses even when the database contains data for both IPv4 and IPv6 addresses. The IPv4 address will be looked up as '::xxx.xxx.xxx.xxx' rather than being remapped to the ::ffff:xxx.xxx.xxx.xxx block allocated for IPv4-mapped IPv6 addresses. 

 If you pass an IPv6 address to a database with only IPv4 data then the found_entry member will be false, but the mmdb_error status will still be MMDB_SUCCESS.

<h3>MMDB_lookup_sockaddr()</h3>

<dl>
<dt>
<dd> 
MMDB_lookup_result_s MMDB_lookup_sockaddr(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb,
                                               &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; const struct sockaddr &amp;nbsp; *const sockaddr,
                                                      &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; int &amp;nbsp; *const mmdb_error);
</dl>
 

 This function looks up an IP address that has already been resolved by getaddrinfo(). 

 Other than not calling getaddrinfo() itself, this function is identical to the MMDB_lookup_string() function.
<dl>
<dt>
<dd> 
int mmdb_error;
MMDB_lookup_result_s result &amp;nbsp;
=
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_lookup_sockaddr(&amp;mmdb, address-&gt;ai_addr, &amp;nbsp; &amp;mmdb_error);
if
    &amp;nbsp;
(MMDB_SUCCESS &amp;nbsp; != &amp;nbsp; mmdb_error) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
if
    &amp;nbsp;
(result.found_entry) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
</dl>

<h3>Data Lookup Functions</h3>

 

 There are three functions for looking up data associated with an IP address.
<dl>
<dt>
<dd> 
int MMDB_get_value(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_s &amp; nbsp; *const start,
                                                     &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_s &amp; nbsp; *const entry_data,
                                                   &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp;...);
int MMDB_vget_value(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_s &amp; nbsp; *const start,
                                                     &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_s &amp; nbsp; *const entry_data,
                                                   &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; va_list va_path);
int MMDB_aget_value(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_s &amp; nbsp; *const start,
                                                     &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_s &amp; nbsp; *const entry_data,
                                                   &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; const char &amp;nbsp; *const &amp;nbsp; *const path);
</dl>
 

 The three functions allow three slightly different calling styles, but they all do the same thing. 

 The first parameter is an MMDB_entry_s value. In most cases this will come from the MMDB_lookup_result_s value returned by MMDB_lookup_string() or MMDB_lookup_sockaddr(). 

 The second parameter is a reference to an MMDB_entry_data_s structure. This will be populated with the data that is being looked up, if any is found. If nothing is found, then the has_data member of this structure will be false. If has_data is true then you can look at the data_type member. 

 The final parameter is a lookup path. The path consists of a set of strings representing either map keys (e.g, &quot;city&quot;) or array indexes (e.g., &quot;0&quot;, &quot;1&quot;, &quot;-1&quot;) to use in the lookup. 

 Negative array indexes will be treated as an offset from the end of the array. For instance, &quot;-1&quot; refers to the last element of the array. 

 The lookup path allows you to navigate a complex data structure. For example, given this data:
<dl>
<dt>
<dd> 
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    "names" : &amp;nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        "en" : &amp;nbsp;
        "Germany",
            &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        "de" : &amp;nbsp;
        "Deutschland" &amp; nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    ,
        &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    "cities" : &amp;nbsp;
    [&amp;nbsp; "Berlin", &amp;nbsp; "Frankfurt" &amp; nbsp; ]
}
</dl>
 

 We could look up the English name with this code:
<dl>
<dt>
<dd> 
MMDB_lookup_result_s result &amp;nbsp;
=
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_lookup_sockaddr(&amp;mmdb, address-&gt;ai_addr, &amp;nbsp; &amp;mmdb_error);
MMDB_entry_data_s entry_data;
int status &amp;nbsp;
=
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_get_value(&amp;result.entry, &amp;nbsp; &amp;entry_data,
                                     &amp;nbsp;
               &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; "names", &amp;nbsp; "en", NULL);
if
    &amp;nbsp;
(MMDB_SUCCESS &amp;nbsp; != &amp;nbsp; status) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
if
    &amp;nbsp;
(entry_data.has_data) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
</dl>
 

 If we wanted to find the first city the lookup path would be &quot;cities&quot;,&nbsp;&quot;0&quot;. If you don't provide a lookup path at all, you'll get the entry which corresponds to the top level map. The lookup path must always end with NULL, regardless of which function you call. 

 The MMDB_get_value function takes a variable number of arguments. All of the arguments after the MMDB_entry_data_s&nbsp;* structure pointer are the lookup path. The last argument must be NULL. 

 The MMDB_vget_value function accepts a va_list as the lookup path. The last element retrieved by va_arg() must be NULL. 

 Finally, the MMDB_aget_value accepts an array of strings as the lookup path. The last member of this array must be NULL. 

 If you want to get all of the entry data at once you can call MMDB_get_entry_data_list() instead. 

 For each of the three functions, the return value is a status code as defined above.

<h3>MMDB_get_entry_data_list()</h3>

<dl>
<dt>
<dd> 
int MMDB_get_entry_data_list(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_s &amp; nbsp; *start,
                                                     &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_list_s &amp; nbsp; **const entry_data_list);
</dl>
 

 This function allows you to get all of the data for a complex data structure at once, rather than looking up each piece using repeated calls to MMDB_get_value().
<dl>
<dt>
<dd> 
MMDB_lookup_result_s result &amp;nbsp;
=
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_lookup_sockaddr(&amp;mmdb, address-&gt;ai_addr, &amp;nbsp; &amp;mmdb_error);
MMDB_entry_data_list_s &amp;nbsp;
*entry_data_list, &amp;nbsp;
*first;
int status &amp;nbsp;
=
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_get_entry_data_list(&amp;result.entry, &amp;nbsp; &amp;entry_data_list);
if
    &amp;nbsp;
(MMDB_SUCCESS &amp;nbsp; != &amp;nbsp; status) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
//&amp;nbsp;save this so we can free this data later
first &amp;nbsp;
= &amp;nbsp;
entry_data_list;
while
    &amp;nbsp;
(1) &amp; nbsp;
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_entry_data_list_s &amp;nbsp;
    *next &amp;nbsp;
    = &amp;nbsp;
    entry_data_list &amp;nbsp;
    = &amp;nbsp;
    entry_data_list-&gt;next;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    if
        &amp;nbsp;
    (NULL &amp; nbsp; == &amp;nbsp; next) &amp; nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        break;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    switch
        &amp;nbsp;
    (next-&gt;entry_data.type) &amp; nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    case MMDB_DATA_TYPE_MAP:
        &amp;nbsp;
        {
            &amp;nbsp;
            ... &amp;nbsp;
        }
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    case MMDB_DATA_TYPE_UTF8_STRING:
        &amp;nbsp;
        {
            &amp;nbsp;
            ... &amp;nbsp;
        }
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        ...
            &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
}
MMDB_free_entry_data_list(first);
</dl>
 

 It's up to you to interpret the entry_data_list data structure. The list is linked in a depth-first traversal. Let's use this structure as an example:
<dl>
<dt>
<dd> 
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    "names" : &amp;nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        "en" : &amp;nbsp;
        "Germany",
            &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        "de" : &amp;nbsp;
        "Deutschland" &amp; nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    ,
        &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    "cities" : &amp;nbsp;
    [&amp;nbsp; "Berlin", &amp;nbsp; "Frankfurt" &amp; nbsp; ]
}
</dl>
 

 The list will consist of the following items:
<dl>
<dt> 1.
<dd> MAP - top level map
<dt> 2.
<dd> UTF8_STRING - &quot;names&quot; key
<dt> 3.
<dd> MAP - map for &quot;names&quot; key
<dt> 4.
<dd> UTF8_STRING - &quot;en&quot; key
<dt> 5.
<dd> UTF8_STRING - value for &quot;en&quot; key
<dt> 6.
<dd> UTF8_STRING - &quot;de&quot; key
<dt> 7.
<dd> UTF8_STRING - value for &quot;de&quot; key
<dt> 8.
<dd> UTF8_STRING - &quot;cities&quot; key
<dt> 9.
<dd> ARRAY - value for &quot;cities&quot; key
<dt>10.
<dd> UTF8_STRING - array[0]
<dt>11.
<dd> UTF8_STRING - array[1]</dl>
 

 The return value of the function is a status code as defined above.

<h3>MMDB_free_entry_data_list()</h3>

<dl>
<dt>
<dd> 
void MMDB_free_entry_data_list(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_list_s &amp; nbsp; *const entry_data_list);
</dl>
 

 The MMDB_get_entry_data_list() and MMDB_get_metadata_as_entry_data_list() functions will allocate the linked list structure from the heap. Call this function to free the MMDB_entry_data_list_s structure.

<h3>MMDB_get_metadata_as_entry_data_list()</h3>

<dl>
<dt>
<dd> 
int MMDB_get_metadata_as_entry_data_list(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb,
                                               &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_list_s &amp; nbsp; **const entry_data_list);
</dl>
 

 This function allows you to retrieve the database metadata as a linked list of MMDB_entry_data_list_s structures. This can be a more convenient way to deal with the metadata than using the metadata structure directly.
<dl>
<dt>
<dd> 
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_entry_data_list_s &amp;nbsp;
*entry_data_list, &amp;nbsp;
*first;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
int status &amp;nbsp;
=
    &amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_get_metadata_as_entry_data_list(&amp;mmdb, &amp;nbsp; &amp;entry_data_list);
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
if
    &amp;nbsp;
(MMDB_SUCCESS &amp;nbsp; != &amp;nbsp; status) &amp; nbsp;
{
    &amp;nbsp;
    ... &amp;nbsp;
}
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
first &amp;nbsp;
= &amp;nbsp;
entry_data_list;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
... &amp;nbsp; //&amp;nbsp;do something with the data
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
&amp;nbsp;
MMDB_free_entry_data_list(first);
</dl>
 

 The return value of the function is a status code as defined above.

<h3>MMDB_dump_entry_data_list()</h3>

<dl>
<dt>
<dd> 
int MMDB_dump_entry_data_list(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; FILE &amp; nbsp; *const stream,
                                             &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_entry_data_list_s &amp; nbsp; *const entry_data_list,
                                                        &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; int indent);
</dl>
 

 This function takes a linked list of MMDB_entry_data_list_s structures and stringifies it to the given stream. The indent parameter is the starting indent level for the generated output. It is incremented for nested data structures (maps, array, etc.). 

 The stream must be a file handle (stdout, etc). If your platform provides something like the GNU open_memstream() you can use that to capture the output as a string. 

 The output is formatted in a JSON-ish fashion, but values are marked with their data type (except for maps and arrays which are shown with &quot;{}&quot; and &quot;[]&quot; respectively). 

 The specific output format may change in future releases, so you should not rely on the specific formatting produced by this function. It is intended to be used to show data to users in a readable way and for debugging purposes. 

 The return value of the function is a status code as defined above.

<h3>MMDB_read_node()</h3>

<dl>
<dt>
<dd> 
int MMDB_read_node(
    &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_s &amp; nbsp; *const mmdb,
                                               &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; uint32_t node_number,
                         &amp;nbsp;
    &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_search_node_s &amp; nbsp; *const node);
</dl>
 

 This reads a specific node in the search tree. The third argument is a reference to an MMDB_search_node_s structure that will be populated by this function. 

 The return value is a status code. If you pass a node_number that is greater than the number of nodes in the database, this function will return MMDB_INVALID_NODE_NUMBER_ERROR, otherwise it will return MMDB_SUCCESS. 

 The first node in the search tree is always node 0. If you wanted to iterate over the whole search tree, you would start by reading node 0 and then following the the records that make up this node, based on the type of each record. If the type is MMDB_RECORD_TYPE_SEARCH_NODE then the record contains an integer for the next node to look up.

<h3>MMDB_lib_version()</h3>

<dl>
<dt>
<dd> 
const char &amp;nbsp;
*MMDB_lib_version(void)
</dl>
 

 This function returns the library version as a string, something like &quot;2.0.0&quot;.

<h2>EXAMPLE</h2>

<dl>
<dt>
<dd> <pre><code>
#include &amp;nbsp; &lt; errno.h&gt;
#include &amp;nbsp; &lt; maxminddb.h&gt;
#include &amp;nbsp; &lt; stdlib.h&gt;
#include &amp;nbsp; &lt; string.h&gt;
int main(int argc, char &amp;nbsp; **argv)
{
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    char &amp;nbsp;
    *filename &amp;nbsp;
    = &amp;nbsp;
    argv[1];
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    char &amp;nbsp;
    *ip_address &amp;nbsp;
    = &amp;nbsp;
    argv[2];
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_s mmdb;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    int status &amp;nbsp;
    = &amp;nbsp;
    MMDB_open(filename, MMDB_MODE_MMAP, &amp;nbsp; &amp;mmdb);
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    if
        &amp;nbsp;
    (MMDB_SUCCESS &amp; nbsp; != &amp;nbsp; status) &amp; nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        fprintf(stderr, &amp;nbsp; "\n&amp;nbsp;&amp;nbsp;Can't open&amp;nbsp;%s -&amp;nbsp;%s\n",
                               &amp;nbsp;
                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; filename, MMDB_strerror(status));
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        if
            &amp;nbsp;
        (MMDB_IO_ERROR &amp; nbsp; == &amp;nbsp; status) &amp; nbsp;
        {
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            fprintf(stderr, &amp;nbsp; "&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;IO error:&amp;nbsp;%s\n", strerror(errno));
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
        }
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        exit(1);
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    int gai_error, mmdb_error;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_lookup_result_s result &amp;nbsp;
    =
        &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_lookup_string(&amp;mmdb, ip_address, &amp;nbsp; &amp;gai_error, &amp;nbsp; &amp;mmdb_error);
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    if
        &amp;nbsp;
    (0 &amp; nbsp; != &amp;nbsp; gai_error) &amp; nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        fprintf(stderr,
                &amp;nbsp;
                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; "\n&amp;nbsp;&amp;nbsp;Error from getaddrinfo for&amp;nbsp;%s -&amp;nbsp;%s\n\n",
                                                                                                                         &amp;nbsp;
                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; ip_address, gai_strerror(gai_error));
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        exit(2);
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    if
        &amp;nbsp;
    (MMDB_SUCCESS &amp; nbsp; != &amp;nbsp; mmdb_error) &amp; nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        fprintf(stderr,
                &amp;nbsp;
                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; "\n&amp;nbsp;&amp;nbsp;Got an error from libmaxminddb:&amp;nbsp;%s\n\n",
                                                                                                                         &amp;nbsp;
                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_strerror(mmdb_error));
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        exit(3);
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_entry_data_list_s &amp;nbsp;
    *entry_data_list &amp;nbsp;
    = &amp;nbsp;
    NULL;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    int exit_code &amp;nbsp;
    = &amp;nbsp;
    0;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    if
        &amp;nbsp;
    (result.found_entry) &amp; nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        int status &amp;nbsp;
        = &amp;nbsp;
        MMDB_get_entry_data_list(&amp;result.entry,
                                 &amp;nbsp;
                                 &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;entry_data_list);
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        if
            &amp;nbsp;
        (MMDB_SUCCESS &amp; nbsp; != &amp;nbsp; status) &amp; nbsp;
        {
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            fprintf(
                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; stderr,
                                                                                                                                &amp;nbsp;
                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; "Got an error looking up the entry data -&amp;nbsp;%s\n",
                                                                                                                         &amp;nbsp;
                &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; MMDB_strerror(status));
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            exit_code &amp;nbsp;
            = &amp;nbsp;
            4;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            goto end;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
        }
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        if
            &amp;nbsp;
        (NULL &amp; nbsp; != &amp;nbsp; entry_data_list) &amp; nbsp;
        {
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            MMDB_dump_entry_data_list(stdout, entry_data_list, 2);
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
            &amp;nbsp;
        }
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    &amp;nbsp;
    else &amp;nbsp;
    {
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        fprintf(
            &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; stderr,
                                                                                                &amp;nbsp;
            &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; "\n&amp;nbsp;&amp;nbsp;No entry for this IP address&amp;nbsp;(%s)&amp;nbsp;was found\n\n",
                                                                                         &amp;nbsp;
            &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; &amp;nbsp; ip_address);
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        exit_code &amp;nbsp;
        = &amp;nbsp;
        5;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
        &amp;nbsp;
    }
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
end:
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_free_entry_data_list(entry_data_list);
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    MMDB_close(&amp;mmdb);
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    &amp;nbsp;
    exit(exit_code);
}
</code></pre></dl>

<h2>THREAD SAFETY</h2>

 

 This library is thread safe when compiled and linked with a thread-safe malloc and free implementation.

<h2>INSTALLATION AND SOURCE</h2>

 

 You can download the latest release of libmaxminddb from GitHub (<a rel="nofollow" HREF="https://github.com/maxmind/libmaxminddb/releases">https://github.com/maxmind/libmaxminddb/releases</a>). 

 Our GitHub repo (<a rel="nofollow" HREF="https://github.com/maxmind/libmaxminddb)">https://github.com/maxmind/libmaxminddb)</a> is publicly available. Please fork it!

<h2>BUG REPORTS AND PULL REQUESTS</h2>

 

 Please report all issues to our GitHub issue tracker (<a rel="nofollow" HREF="https://github.com/maxmind/libmaxminddb/issues">https://github.com/maxmind/libmaxminddb/issues</a>). We welcome bug reports and pull requests. Please note that pull requests are greatly preferred over patches.

<h2>AUTHORS</h2>

 

 This library was written by Boris Zentner (bzentner [at] maxmind.com) and Dave Rolsky (drolsky [at] maxmind.com).

<h2>COPYRIGHT AND LICENSE</h2>

 

 Copyright 2013-2014 MaxMind, Inc. 

 Licensed under the Apache License, Version 2.0 (the &quot;License&quot;); you may not use this file except in compliance with the License. You may obtain a copy of the License at
<dl>
<dt>
<dd> <pre>
<a rel="nofollow" HREF="http://www.apache.org/licenses/LICENSE-2.0">http://www.apache.org/licenses/LICENSE-2.0</a>
</pre></dl>
 

 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an &quot;AS IS&quot; BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-mmdblookup/">mmdblookup</a>(1) 

<h2>Index</h2>


