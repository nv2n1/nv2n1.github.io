---
title: "create_type(7)"
name: "create_type"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_type/"
description: "CREATE TYPE – define a new data type"
---

<p>CREATE TYPE &#8211; define a new data type </p>
<h2>Synopsis</h2>
<pre>CREATE TYPE <i>name</i> AS
 ( <i>attribute_name</i> <i>data_type</i> [, ... ] )
CREATE TYPE <i>name</i> AS ENUM
 ( '<i>label</i>' [, ... ] )
CREATE TYPE <i>name</i> (
 INPUT = <i>input_function</i>,
 OUTPUT = <i>output_function</i>
 [ , RECEIVE = <i>receive_function</i> ]
 [ , SEND = <i>send_function</i> ]
 [ , TYPMOD_IN = <i>type_modifier_input_function</i> ]
 [ , TYPMOD_OUT = <i>type_modifier_output_function</i> ]
 [ , ANALYZE = <i>analyze_function</i> ]
 [ , INTERNALLENGTH = { <i>internallength</i> | VARIABLE } ]
 [ , PASSEDBYVALUE ]
 [ , ALIGNMENT = <i>alignment</i> ]
 [ , STORAGE = <i>storage</i> ]
 [ , LIKE = <i>like_type</i> ]
 [ , CATEGORY = <i>category</i> ]
 [ , PREFERRED = <i>preferred</i> ]
 [ , DEFAULT = <i>default</i> ]
 [ , ELEMENT = <i>element</i> ]
 [ , DELIMITER = <i>delimiter</i> ]
)
CREATE TYPE <i>name</i></pre>
<h2>Description</h2>
<p><code>CREATE TYPE</code> registers a new data type for use in the current database. The user who defines a type becomes its owner. </p>
<p> If a schema name is given then the type is created in the specified schema. Otherwise it is created in the current schema. The type name must be distinct from the name of any existing type or domain in the same schema. (Because tables have associated data types, the type name must also be distinct from the name of any existing table in the same schema.)</p>
<h3>Composite Types</h3>
<p>The first form of <code>CREATE TYPE</code> creates a composite type. The composite type is specified by a list of attribute names and data types. This is essentially the same as the row type of a table, but using <code>CREATE TYPE</code> avoids the need to create an actual table when all that is wanted is to define a type. A stand-alone composite type is useful as the argument or return type of a function.</p>
<h3>Enumerated Types</h3>
<p>The second form of <code>CREATE TYPE</code> creates an enumerated (enum) type, as described in in the documentation. Enum types take a list of one or more quoted labels, each of which must be less than <code>NAMEDATALEN</code> bytes long (64 in a standard PostgreSQL build).</p>
<h3>Base Types</h3>
<p>The third form of <code>CREATE TYPE</code> creates a new base type (scalar type). To create a new base type, you must be a superuser. (This restriction is made because an erroneous type definition could confuse or even crash the server.) </p>
<p> The parameters can appear in any order, not only that illustrated above, and most are optional. You must register two or more functions (using <code>CREATE FUNCTION</code>) before defining the type. The support functions <i>input_function</i> and <i>output_function</i> are required, while the functions <i>receive_function</i>, <i>send_function</i>, <i>type_modifier_input_function</i>, <i>type_modifier_output_function</i> and <i>analyze_function</i> are optional. Generally these functions have to be coded in C or another low-level language. </p>
<p> The <i>input_function</i> converts the type&#8217;s external textual representation to the internal representation used by the operators and functions defined for the type. <i>output_function</i> performs the reverse transformation. The input function can be declared as taking one argument of type <code>cstring</code>, or as taking three arguments of types <code>cstring</code>, <code>oid</code>, <code>integer</code>. The first argument is the input text as a C string, the second argument is the type&#8217;s own OID (except for array types, which instead receive their element type&#8217;s OID), and the third is the typmod of the destination column, if known (-1 will be passed if not). The input function must return a value of the data type itself. Usually, an input function should be declared STRICT; if it is not, it will be called with a NULL first parameter when reading a NULL input value. The function must still return NULL in this case, unless it raises an error. (This case is mainly meant to support domain input functions, which might need to reject NULL inputs.) The output function must be declared as taking one argument of the new data type. The output function must return type <code>cstring</code>. Output functions are not invoked for NULL values. </p>
<p> The optional <i>receive_function</i> converts the type&#8217;s external binary representation to the internal representation. If this function is not supplied, the type cannot participate in binary input. The binary representation should be chosen to be cheap to convert to internal form, while being reasonably portable. (For example, the standard integer data types use network byte order as the external binary representation, while the internal representation is in the machine&#8217;s native byte order.) The receive function should perform adequate checking to ensure that the value is valid. The receive function can be declared as taking one argument of type <code>internal</code>, or as taking three arguments of types <code>internal</code>, <code>oid</code>, <code>integer</code>. The first argument is a pointer to a <code>StringInfo</code> buffer holding the received byte string; the optional arguments are the same as for the text input function. The receive function must return a value of the data type itself. Usually, a receive function should be declared STRICT; if it is not, it will be called with a NULL first parameter when reading a NULL input value. The function must still return NULL in this case, unless it raises an error. (This case is mainly meant to support domain receive functions, which might need to reject NULL inputs.) Similarly, the optional <i>send_function</i> converts from the internal representation to the external binary representation. If this function is not supplied, the type cannot participate in binary output. The send function must be declared as taking one argument of the new data type. The send function must return type <code>bytea</code>. Send functions are not invoked for NULL values. </p>
<p> You should at this point be wondering how the input and output functions can be declared to have results or arguments of the new type, when they have to be created before the new type can be created. The answer is that the type should first be defined as a <i>shell type</i>, which is a placeholder type that has no properties except a name and an owner. This is done by issuing the command CREATE TYPE <i>name</i>, with no additional parameters. Then the I/O functions can be defined referencing the shell type. Finally, <code>CREATE TYPE</code> with a full definition replaces the shell entry with a complete, valid type definition, after which the new type can be used normally. </p>
<p> The optional <i>type_modifier_input_function</i> and <i>type_modifier_output_function</i> are needed if the type supports modifiers, that is optional constraints attached to a type declaration, such as <a href="/docs/linux/man/5-char/">char</a>(5) or numeric(30,2). PostgreSQL allows user-defined types to take one or more simple constants or identifiers as modifiers. However, this information must be capable of being packed into a single non-negative integer value for storage in the system catalogs. The <i>type_modifier_input_function</i> is passed the declared modifier(s) in the form of a <code>cstring</code> array. It must check the values for validity (throwing an error if they are wrong), and if they are correct, return a single non-negative <code>integer</code> value that will be stored as the column &#8220;typmod&#8221;. Type modifiers will be rejected if the type does not have a <i>type_modifier_input_function</i>. The <i>type_modifier_output_function</i> converts the internal integer typmod value back to the correct form for user display. It must return a <code>cstring</code> value that is the exact string to append to the type name; for example <code>numeric</code>&#8216;s function might return (30,2). It is allowed to omit the <i>type_modifier_output_function</i>, in which case the default display format is just the stored typmod integer value enclosed in parentheses. </p>
<p> The optional <i>analyze_function</i> performs type-specific statistics collection for columns of the data type. By default, <code>ANALYZE</code> will attempt to gather statistics using the type&#8217;s &#8220;equals&#8221; and &#8220;less-than&#8221; operators, if there is a default b-tree operator class for the type. For non-scalar types this behavior is likely to be unsuitable, so it can be overridden by specifying a custom analysis function. The analysis function must be declared to take a single argument of type <code>internal</code>, and return a <code>boolean</code> result. The detailed API for analysis functions appears in <i>src/include/commands/vacuum.h</i>. </p>
<p> While the details of the new type&#8217;s internal representation are only known to the I/O functions and other functions you create to work with the type, there are several properties of the internal representation that must be declared to PostgreSQL. Foremost of these is <i>internallength</i>. Base data types can be fixed-length, in which case <i>internallength</i> is a positive integer, or variable length, indicated by setting <i>internallength</i> to VARIABLE. (Internally, this is represented by setting typlen to -1.) The internal representation of all variable-length types must start with a 4-byte integer giving the total length of this value of the type. </p>
<p> The optional flag PASSEDBYVALUE indicates that values of this data type are passed by value, rather than by reference. You cannot pass by value types whose internal representation is larger than the size of the <code>Datum</code> type (4 bytes on most machines, 8 bytes on a few). </p>
<p> The <i>alignment</i> parameter specifies the storage alignment required for the data type. The allowed values equate to alignment on 1, 2, 4, or 8 byte boundaries. Note that variable-length types must have an alignment of at least 4, since they necessarily contain an <code>int4</code> as their first component. </p>
<p> The <i>storage</i> parameter allows selection of storage strategies for variable-length data types. (Only plain is allowed for fixed-length types.) plain specifies that data of the type will always be stored in-line and not compressed. extended specifies that the system will first try to compress a long data value, and will move the value out of the main table row if it&#8217;s still too long. external allows the value to be moved out of the main table, but the system will not try to compress it. main allows compression, but discourages moving the value out of the main table. (Data items with this storage strategy might still be moved out of the main table if there is no other way to make a row fit, but they will be kept in the main table preferentially over extended and external items.) </p>
<p> The <i>like_type</i> parameter provides an alternative method for specifying the basic representation properties of a data type: copy them from some existing type. The values of <i>internallength</i>, <i>passedbyvalue</i>, <i>alignment</i>, and <i>storage</i> are copied from the named type. (It is possible, though usually undesirable, to override some of these values by specifying them along with the LIKE clause.) Specifying representation this way is especially useful when the low-level implementation of the new type &#8220;piggybacks&#8221; on an existing type in some fashion. </p>
<p> The <i>category</i> and <i>preferred</i> parameters can be used to help control which implicit cast will be applied in ambiguous situations. Each data type belongs to a category named by a single ASCII character, and each type is either &#8220;preferred&#8221; or not within its category. The parser will prefer casting to preferred types (but only from other types within the same category) when this rule is helpful in resolving overloaded functions or operators. For more details see in the documentation. For types that have no implicit casts to or from any other types, it is sufficient to leave these settings at the defaults. However, for a group of related types that have implicit casts, it is often helpful to mark them all as belonging to a category and select one or two of the &#8220;most general&#8221; types as being preferred within the category. The <i>category</i> parameter is especially useful when adding a user-defined type to an existing built-in category, such as the numeric or string types. However, it is also possible to create new entirely-user-defined type categories. Select any ASCII character other than an upper-case letter to name such a category. </p>
<p> A default value can be specified, in case a user wants columns of the data type to default to something other than the null value. Specify the default with the DEFAULT key word. (Such a default can be overridden by an explicit DEFAULT clause attached to a particular column.) </p>
<p> To indicate that a type is an array, specify the type of the array elements using the ELEMENT key word. For example, to define an array of 4-byte integers (<code>int4</code>), specify ELEMENT = int4. More details about array types appear below. </p>
<p> To indicate the delimiter to be used between values in the external representation of arrays of this type, <i>delimiter</i> can be set to a specific character. The default delimiter is the comma (,). Note that the delimiter is associated with the array element type, not the array type itself.</p>
<h3>Array Types</h3>
<p>Whenever a user-defined type is created, PostgreSQL automatically creates an associated array type, whose name consists of the base type&#8217;s name prepended with an underscore, and truncated if necessary to keep it less than <code>NAMEDATALEN</code> bytes long. (If the name so generated collides with an existing type name, the process is repeated until a non-colliding name is found.) This implicitly-created array type is variable length and uses the built-in input and output functions array_in and array_out. The array type tracks any changes in its element type&#8217;s owner or schema, and is dropped if the element type is. </p>
<p> You might reasonably ask why there is an <code>ELEMENT</code> option, if the system makes the correct array type automatically. The only case where it&#8217;s useful to use <code>ELEMENT</code> is when you are making a fixed-length type that happens to be internally an array of a number of identical things, and you want to allow these things to be accessed directly by subscripting, in addition to whatever operations you plan to provide for the type as a whole. For example, type <code>point</code> is represented as just two floating-point numbers, which it allows to be accessed as point[0] and point[1]. Note that this facility only works for fixed-length types whose internal form is exactly a sequence of identical fixed-length fields. A subscriptable variable-length type must have the generalized internal representation used by array_in and array_out. For historical reasons (i.e., this is clearly wrong but it&#8217;s far too late to change it), subscripting of fixed-length array types starts from zero, rather than from one as for variable-length arrays.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of a type to be created.</p>
<dt><i>attribute_name</i></p>
<dd>The name of an attribute (column) for the composite type.</p>
<dt><i>data_type</i></p>
<dd>The name of an existing data type to become a column of the composite type.</p>
<dt><i>label</i></p>
<dd>A string literal representing the textual label associated with one value of an enum type.</p>
<dt><i>input_function</i></p>
<dd>The name of a function that converts data from the type&#8217;s external textual form to its internal form.</p>
<dt><i>output_function</i></p>
<dd>The name of a function that converts data from the type&#8217;s internal form to its external textual form.</p>
<dt><i>receive_function</i></p>
<dd>The name of a function that converts data from the type&#8217;s external binary form to its internal form.</p>
<dt><i>send_function</i></p>
<dd>The name of a function that converts data from the type&#8217;s internal form to its external binary form.</p>
<dt><i>type_modifier_input_function</i></p>
<dd>The name of a function that converts an array of modifier(s) for the type into internal form.</p>
<dt><i>type_modifier_output_function</i></p>
<dd>The name of a function that converts the internal form of the type&#8217;s modifier(s) to external textual form.</p>
<dt><i>analyze_function</i></p>
<dd>The name of a function that performs statistical analysis for the data type.</p>
<dt><i>internallength</i></p>
<dd>A numeric constant that specifies the length in bytes of the new type&#8217;s internal representation. The default assumption is that it is variable-length.</p>
<dt><i>alignment</i></p>
<dd>The storage alignment requirement of the data type. If specified, it must be char, int2, int4, or double; the default is int4.</p>
<dt><i>storage</i></p>
<dd>The storage strategy for the data type. If specified, must be plain, external, extended, or main; the default is plain.</p>
<dt><i>like_type</i></p>
<dd>The name of an existing data type that the new type will have the same representation as. The values of <i>internallength</i>, <i>passedbyvalue</i>, <i>alignment</i>, and <i>storage</i> are copied from that type, unless overridden by explicit specification elsewhere in this <code>CREATE TYPE</code> command.</p>
<dt><i>category</i></p>
<dd>The category code (a single ASCII character) for this type. The default is &#8216;U&#8217; for &#8220;user-defined type&#8221;. Other standard category codes can be found in in the documentation. You may also choose other ASCII characters in order to create custom categories.</p>
<dt><i>preferred</i></p>
<dd>True if this type is a preferred type within its type category, else false. The default is false. Be very careful about creating a new preferred type within an existing type category, as this could cause surprising changes in behavior.</p>
<dt><i>default</i></p>
<dd>The default value for the data type. If this is omitted, the default is null.</p>
<dt><i>element</i></p>
<dd>The type being created is an array; this specifies the type of the array elements.</p>
<dt><i>delimiter</i></p>
<dd>The delimiter character to be used between values in arrays made of this type.</dl>
<h2>Notes</h2>
<p>Because there are no restrictions on use of a data type once it&#8217;s been created, creating a base type is tantamount to granting public execute permission on the functions mentioned in the type definition. This is usually not an issue for the sorts of functions that are useful in a type definition. But you might want to think twice before designing a type in a way that would require &#8220;secret&#8221; information to be used while converting it to or from external form. </p>
<p> Before PostgreSQL version 8.3, the name of a generated array type was always exactly the element type&#8217;s name with one underscore character (_) prepended. (Type names were therefore restricted in length to one less character than other names.) While this is still usually the case, the array type name may vary from this in case of maximum-length names or collisions with user type names that begin with underscore. Writing code that depends on this convention is therefore deprecated. Instead, use <code>pg_type</code>.<code>typarray</code> to locate the array type associated with a given type. </p>
<p> It may be advisable to avoid using type and table names that begin with underscore. While the server will change generated array type names to avoid collisions with user-given names, there is still risk of confusion, particularly with old client software that may assume that type names beginning with underscores always represent arrays. </p>
<p> Before PostgreSQL version 8.2, the syntax CREATE TYPE <i>name</i> did not exist. The way to create a new base type was to create its input function first. In this approach, PostgreSQL will first see the name of the new data type as the return type of the input function. The shell type is implicitly created in this situation, and then it can be referenced in the definitions of the remaining I/O functions. This approach still works, but is deprecated and might be disallowed in some future release. Also, to avoid accidentally cluttering the catalogs with shell types as a result of simple typos in function definitions, a shell type will only be made this way when the input function is written in C. </p>
<p> In PostgreSQL versions before 7.3, it was customary to avoid creating a shell type at all, by replacing the functions&#8217; forward references to the type name with the placeholder pseudotype <code>opaque</code>. The <code>cstring</code> arguments and results also had to be declared as <code>opaque</code> before 7.3. To support loading of old dump files, <code>CREATE TYPE</code> will accept I/O functions declared using <code>opaque</code>, but it will issue a notice and change the function declarations to use the correct types.</p>
<h2>Examples</h2>
<p>This example creates a composite type and uses it in a function definition: </p>
<pre>CREATE TYPE compfoo AS (f1 int, f2 text);
CREATE FUNCTION getfoo() RETURNS SETOF compfoo AS $$
 SELECT fooid, fooname FROM foo
$$ LANGUAGE SQL;</pre>
<p>This example creates an enumerated type and uses it in a table definition: </p>
<pre>CREATE TYPE bug_status AS ENUM ('new', 'open', 'closed');
CREATE TABLE bug (
 id serial,
 description text,
 status bug_status
);</pre>
<p>This example creates the base data type <code>box</code> and then uses the type in a table definition: </p>
<pre><code>CREATE TYPE bigobj (
INPUT = lo_filein, OUTPUT = lo_fileout,
INTERNALLENGTH = VARIABLE
);
CREATE TABLE big_objs (
id integer,
obj bigobj
);</code></pre>
<p> If the internal structure of <code>box</code> were an array of four <code>float4</code> elements, we might instead use: </p>
<pre>CREATE TYPE box (
 INTERNALLENGTH = 16,
 INPUT = my_box_in_function,
 OUTPUT = my_box_out_function,
 ELEMENT = float4
);</pre>
<p>which would allow a box value&#8217;s component numbers to be accessed by subscripting. Otherwise the type behaves the same as before. This example creates a large object type and uses it in a table definition: </p>
<pre><code>CREATE TYPE bigobj (
INPUT = lo_filein, OUTPUT = lo_fileout,
INTERNALLENGTH = VARIABLE
);
CREATE TABLE big_objs (
id integer,
obj bigobj
);</code></pre>
<p> More examples, including suitable input and output functions, are in in the documentation.</p>
<h2>Compatibility</h2>
<p>This <code>CREATE TYPE</code> command is a PostgreSQL extension. There is a <code>CREATE TYPE</code> statement in the SQL standard that is rather different in detail.</p>
<h2>See Also</h2>
<p>CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)], DROP TYPE [<code><a href="/docs/linux/man/7-drop_type/">drop_type</a></code>(7)], ALTER TYPE [<code><a href="/docs/linux/man/7-alter_type/">alter_type</a></code>(7)], CREATE DOMAIN [<code><a href="/docs/linux/man/7-create_domain/">create_domain</a></code>(7)] </p>
