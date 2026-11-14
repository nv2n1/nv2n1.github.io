---
title: "mlx5dv_dump_dr_domain(3)"
name: "mlx5dv_dump_dr_domain"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_dump_dr_domain/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_dump_dr_domain - Dump DR Domain 

 mlx5dv_dump_dr_table - Dump DR Table 

 mlx5dv_dump_dr_matcher - Dump DR Matcher 

 mlx5dv_dump_dr_rule - Dump DR Rule 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
int mlx5dv_dump_dr_domain(FILE *fout, struct mlx5dv_dr_domain *domain);
int mlx5dv_dump_dr_table(FILE *fout, struct mlx5dv_dr_table *table);
int mlx5dv_dump_dr_matcher(FILE *fout, struct mlx5dv_dr_matcher *matcher);
int mlx5dv_dump_dr_rule(FILE *fout, struct mlx5dv_dr_rule *rule);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 The Dump API (mlx5dv_dump_*) allows the dumping of the existing rdma-core resources to the provided file. The output file format is vendor specific. 

 mlx5dv_dump_dr_domain() dumps a DR Domain object properties to a specified file. 

 mlx5dv_dump_dr_table() dumps a DR Table object properties to a specified file. 

 mlx5dv_dump_dr_matcher() dumps a DR Matcher object properties to a specified file. 

 mlx5dv_dump_dr_rule() dumps a DR Rule object properties to a specified file.

<h2>RETURN VALUE</h2>

 

 The API calls returns 0 on success, or the value of errno on failure (which indicates the failure reason). The calls are blocking - function returns only when all related resources info is written to the file.

<h2>AUTHOR</h2>

 

 Yevgeny Kliteynik &lt;kliteyn [at] mellanox.com&gt; Muhammad Sammar &lt;muhammads [at] mellanox.com&gt; 

<h2>Index</h2>


