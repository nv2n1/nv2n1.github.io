---
title: "mlx5dv_create_mkey(3)"
name: "mlx5dv_create_mkey"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_create_mkey/"
---

<h2 class="name">NAME</h2>
 

 

 mlx5dv_create_mkey - Creates an indirect mkey 

 mlx5dv_create_mkey - Destroys an indirect mkey 

<h2>SYNOPSIS</h2>

<dl>
<dt>
<dd> <pre><code>
#include &lt;infiniband/mlx5dv.h&gt;
struct mlx5dv_mkey_init_attr {
    struct ibv_pd *pd;
    uint32_t create_flags;
    uint16_t max_entries;
};
struct mlx5dv_mkey {
    uint32_t lkey;
    uint32_t rkey;
};
struct mlx5dv_mkey *
mlx5dv_create_mkey(struct mlx5dv_mkey_init_attr *mkey_init_attr);
int mlx5dv_destroy_mkey(struct mlx5dv_mkey *mkey);
</code></pre></dl>

<h2>DESCRIPTION</h2>

 

 Create / destroy an indirect mkey. 

 Create an indirect mkey to enable application uses its specific device functionality.

<h2>ARGUMENTS</h2>

 

 ##mkey_init_attr##
<dl>
<dt>pd
<dd> ibv protection domain.
<dt>create_flags
<dd> MLX5DV_MKEY_INIT_ATTR_FLAGS_INDIRECT: Indirect mkey is being created.
<dt>max_entries
<dd> Requested max number of pointed entries by this indirect mkey. The function will update the mkey_init_attr-&gt;max_entries with the actual mkey value that was created; it will be greater than or equal to the value requested.</dl>

<h2>RETURN VALUE</h2>

 

 Upon success mlx5dv_create_mkey will return a new struct mlx5dv_mkey on error NULL will be returned and errno will be set. 

 Upon success destroy 0 is returned or the value of errno on a failure.

<h2>Notes</h2>

 

 To let this functionality works a DEVX context should be opened by using mlx5dv_open_device.

<h2>SEE ALSO</h2>

 

 mlx5dv_open_device 

 #AUTHOR 

 Yishai Hadas &lt;yishaih [at] mellanox.com&gt; 

<h2>Index</h2>


