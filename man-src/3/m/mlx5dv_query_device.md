---
title: "mlx5dv_query_device(3)"
name: "mlx5dv_query_device"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mlx5dv_query_device/"
description: "mlx5dv_query_device – Query device capabilities specific to mlx5"
---

<p>mlx5dv_query_device &#8211; Query device capabilities specific to mlx5 </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;infiniband/mlx5dv.h&gt;</code>
<code>int mlx5dv_query_device(struct ibv_context *ctx_in,</code>
<code> struct mlx5dv_context *attrs_out);</code></pre>
<h2>Description</h2>
<p><code>mlx5dv_query_device()</code> Query HW device-specific information which is important for data-path, but isn&#8217;t provided by <code><a href="/docs/linux/man/3-ibv_query_device/">ibv_query_device</a></code>(3). </p>
<p> This function returns version, flags and compatibility mask. The version represents the format of the internal hardware structures that mlx5dv.h represents. Additions of new fields to the existed structures are handled by comp_mask field. </p>
<pre>struct mlx5dv_sw_parsing_caps {
uint32_t sw_parsing_offloads; /* Use enum mlx5dv_sw_parsing_offloads */
uint32_t supported_qpts;
};
struct mlx5dv_striding_rq_caps {
uint32_t min_single_stride_log_num_of_bytes; /* min log size of each stride */
uint32_t max_single_stride_log_num_of_bytes; /* max log size of each stride */
uint32_t min_single_wqe_log_num_of_strides; /* min log number of strides per WQE */
uint32_t max_single_wqe_log_num_of_strides; /* max log number of strides per WQE */
uint32_t supported_qpts;
};
struct mlx5dv_context {
uint8_t version;
uint64_t flags;
uint64_t comp_mask; /* Use enum mlx5dv_context_comp_mask */
struct mlx5dv_cqe_comp_caps cqe_comp_caps;
struct mlx5dv_sw_parsing_caps sw_parsing_caps;
uint32_t tunnel_offloads_caps;
uint32_t max_dynamic_bfregs /* max blue-flame registers that can be dynamiclly allocated */
uint64_t max_clock_info_update_nsec;
uint32_t flow_action_flags; /* use enum mlx5dv_flow_action_cap_flags */
uint32_t dc_odp_caps; /* use enum ibv_odp_transport_cap_bits */
void *hca_core_clock; /* points to a memory location that is mapped to the HCA's core clock */
};
enum mlx5dv_context_flags {
/*
 * This flag indicates if CQE version 0 or 1 is needed.
 */
 MLX5DV_CONTEXT_FLAGS_CQE_V1 = (1 &lt;&lt; 0),
 MLX5DV_CONTEXT_FLAGS_OBSOLETE = (1 &lt;&lt; 1), /* Obsoleted, don't use */
 MLX5DV_CONTEXT_FLAGS_MPW_ALLOWED = (1 &lt;&lt; 2), /* Multi packet WQE is allowed */
 MLX5DV_CONTEXT_FLAGS_ENHANCED_MPW = (1 &lt;&lt; 3), /* Enhanced multi packet WQE is supported or not */
 MLX5DV_CONTEXT_FLAGS_CQE_128B_COMP = (1 &lt;&lt; 4), /* Support CQE 128B compression */
 MLX5DV_CONTEXT_FLAGS_CQE_128B_PAD = (1 &lt;&lt; 5), /* Support CQE 128B padding */
 MLX5DV_CONTEXT_FLAGS_PACKET_BASED_CREDIT_MODE = (1 &lt;&lt; 6), /* Support packet based credit mode in RC QP */
};
enum mlx5dv_context_comp_mask {
MLX5DV_CONTEXT_MASK_CQE_COMPRESION = 1 &lt;&lt; 0,
MLX5DV_CONTEXT_MASK_SWP = 1 &lt;&lt; 1,
MLX5DV_CONTEXT_MASK_STRIDING_RQ = 1 &lt;&lt; 2,
MLX5DV_CONTEXT_MASK_TUNNEL_OFFLOADS = 1 &lt;&lt; 3,
MLX5DV_CONTEXT_MASK_DYN_BFREGS = 1 &lt;&lt; 4,
MLX5DV_CONTEXT_MASK_CLOCK_INFO_UPDATE = 1 &lt;&lt; 5,
MLX5DV_CONTEXT_MASK_FLOW_ACTION_FLAGS = 1 &lt;&lt; 6,
MLX5DV_CONTEXT_MASK_DC_ODP_CAPS = 1 &lt;&lt; 7,
MLX5DV_CONTEXT_MASK_HCA_CORE_CLOCK = 1 &lt;&lt; 8,
};
enum enum mlx5dv_sw_parsing_offloads {
MLX5DV_SW_PARSING = 1 &lt;&lt; 0,
MLX5DV_SW_PARSING_CSUM = 1 &lt;&lt; 1,
MLX5DV_SW_PARSING_LSO = 1 &lt;&lt; 2,
};
enum mlx5dv_tunnel_offloads {
MLX5DV_RAW_PACKET_CAP_TUNNELED_OFFLOAD_VXLAN = 1 &lt;&lt; 0,
MLX5DV_RAW_PACKET_CAP_TUNNELED_OFFLOAD_GRE = 1 &lt;&lt; 1,
MLX5DV_RAW_PACKET_CAP_TUNNELED_OFFLOAD_GENEVE = 1 &lt;&lt; 2,
};
enum mlx5dv_flow_action_cap_flags {
MLX5DV_FLOW_ACTION_FLAGS_ESP_AES_GCM = 1 &lt;&lt; 0, /* Flow action ESP (with AES_GCM keymat) is supported */
MLX5DV_FLOW_ACTION_FLAGS_ESP_AES_GCM_REQ_METADATA = 1 &lt;&lt; 1, /* Flow action ESP always return metadata in the payload */
MLX5DV_FLOW_ACTION_FLAGS_ESP_AES_GCM_SPI_STEERING = 1 &lt;&lt; 2, /* ESP (with AESGCM keymat) Supports matching by SPI (rather than hashing against SPI) */
MLX5DV_FLOW_ACTION_FLAGS_ESP_AES_GCM_FULL_OFFLOAD = 1 &lt;&lt; 3, /* Flow action ESP supports full offload (with AES_GCM keymat) */
MLX5DV_FLOW_ACTION_FLAGS_ESP_AES_GCM_TX_IV_IS_ESN = 1 &lt;&lt; 4, /* Flow action ESP (with AES_GCM keymat), ESN comes implicitly from IV. */
};</pre>
<h2>Return Value</h2>
<p>0 on success or the value of errno on failure (which indicates the failure reason).</p>
<h2>Notes</h2>
<p>&nbsp;*&nbsp;Compatibility mask&nbsp;(comp_mask)&nbsp;is in/out field.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-mlx5dv/">mlx5dv</a></code>(7), <code><a href="/docs/linux/man/3-ibv_query_device/">ibv_query_device</a></code>(3)</p>
<h2>Authors</h2>
<dl COMPACT>
<dt>Leon Romanovsky &lt;leonro [at] mellanox.com&gt;</p>
<dd></dl>
