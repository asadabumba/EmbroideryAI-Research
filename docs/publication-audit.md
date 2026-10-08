# Publication audit

## Scope

The source tree was inspected as a publication source, not modified. The audit found **23,954 non-cache files** outside the primary Git metadata, including **327 tracked** and **22 visible untracked** files. Large ignored research areas were classified by directory; every tracked and visible untracked path is listed below.

## Classification vocabulary

- `KEEP_PUBLIC` — safe to copy without semantic change.
- `SANITIZE_AND_PUBLISH` — useful material published only after removing private paths, hashes, proprietary inventories, or local assumptions.
- `RESEARCH_ONLY` — valuable private tooling or evidence not suitable for this offline public snapshot.
- `PROPRIETARY_EXCLUDE` — third-party, customer-like, binary, capture, or redistribution-sensitive material.
- `LOCAL_ONLY` — workstation configuration, prompts, caches, environment state, or local orchestration.
- `REDUNDANT` — duplicate kits, generated copies, archives, or nested checkouts.
- `UNKNOWN_REVIEW` — not needed for this snapshot and requires a separate human publication decision.

## Bulk directory classification

| Source area | Classification | Reason |
|---|---|---|
| `archive/` | `PROPRIETARY_EXCLUDE` | Third-party installation media, binaries, manuals, and executable artifacts. |
| `dataset/` | `PROPRIETARY_EXCLUDE` | Raw and derived design corpus, customer-like samples, and generated validation data. |
| `logs/` | `RESEARCH_ONLY` | Runtime logs, captures, traces, generated reports, and preserved failure evidence. |
| `[-OtherParameters/` | `LOCAL_ONLY` | Local package-manager and machine state. |
| `.venv/`, caches | `LOCAL_ONLY` | Environment and generated caches. |
| nested tool checkouts | `REDUNDANT` | Third-party or duplicated repositories not part of the public project. |

## Version-control-visible summary

| Classification | File count |
|---|---:|
| `LOCAL_ONLY` | 19 |
| `PROPRIETARY_EXCLUDE` | 3 |
| `REDUNDANT` | 10 |
| `RESEARCH_ONLY` | 305 |
| `SANITIZE_AND_PUBLISH` | 10 |
| `UNKNOWN_REVIEW` | 2 |

The public snapshot was created from a small sanitized subset. No raw source file was copied merely because it was tracked; publication suitability was evaluated independently of Git status.

## Complete tracked/untracked classification

| Source-relative path | State | Classification |
|---|---|---|
| `.gitignore` | tracked | `SANITIZE_AND_PUBLISH` |
| `AUDIT_README.md` | tracked | `RESEARCH_ONLY` |
| `AUTOPILOT_STATUS.md` | tracked | `RESEARCH_ONLY` |
| `EmbroideryAI_audit.zip` | tracked | `PROPRIETARY_EXCLUDE` |
| `EmbroideryAI_audit_kit.zip` | tracked | `PROPRIETARY_EXCLUDE` |
| `EmbroideryAI_audit_kit/AUDIT_README.md` | tracked | `REDUNDANT` |
| `EmbroideryAI_audit_kit/audit/audit_pipeline.py` | tracked | `REDUNDANT` |
| `EmbroideryAI_audit_kit/pytest.ini` | tracked | `REDUNDANT` |
| `EmbroideryAI_audit_kit/requirements-dev.txt` | tracked | `REDUNDANT` |
| `EmbroideryAI_audit_kit/tests/conftest.py` | tracked | `REDUNDANT` |
| `EmbroideryAI_audit_kit/tests/integration/test_corpus.py` | tracked | `REDUNDANT` |
| `EmbroideryAI_audit_kit/tests/unit/test_ddd_parser_helpers.py` | tracked | `REDUNDANT` |
| `EmbroideryAI_audit_kit/tests/unit/test_dst_parser_unit.py` | tracked | `REDUNDANT` |
| `EmbroideryAI_audit_kit/tests/unit/test_rank_logic.py` | tracked | `REDUNDANT` |
| `HANDOFF.md` | tracked | `RESEARCH_ONLY` |
| `MANIFEST.json` | tracked | `UNKNOWN_REVIEW` |
| `README.md` | tracked | `SANITIZE_AND_PUBLISH` |
| `agent/experiment_runner.py` | tracked | `RESEARCH_ONLY` |
| `agent/frida_runner.py` | tracked | `RESEARCH_ONLY` |
| `agent/wilcom_control.py` | tracked | `RESEARCH_ONLY` |
| `audit/audit_pipeline.py` | tracked | `REDUNDANT` |
| `config/local_positioned_authority_v1.json` | tracked | `UNKNOWN_REVIEW` |
| `dataset/paired/strict_pairs.json` | tracked | `PROPRIETARY_EXCLUDE` |
| `dev_autopilot.ps1` | tracked | `LOCAL_ONLY` |
| `docs/kalyaska_shadow_scope.md` | tracked | `RESEARCH_ONLY` |
| `docs/re_state.md` | tracked | `RESEARCH_ONLY` |
| `hook_dd_producer.py` | tracked | `LOCAL_ONLY` |
| `hook_dd_producer_dump.py` | tracked | `LOCAL_ONLY` |
| `hook_dd_producer_stalker.py` | tracked | `LOCAL_ONLY` |
| `hook_designdoc_debug.py` | tracked | `LOCAL_ONLY` |
| `hook_designdoc_stack.py` | tracked | `LOCAL_ONLY` |
| `hook_designdoc_wait.py` | tracked | `LOCAL_ONLY` |
| `hook_designdoc_write.py` | tracked | `LOCAL_ONLY` |
| `hook_save_trace.py` | tracked | `LOCAL_ONLY` |
| `hook_serialize.py` | tracked | `LOCAL_ONLY` |
| `hook_storage_streams.py` | tracked | `LOCAL_ONLY` |
| `install.ps1` | tracked | `LOCAL_ONLY` |
| `notebooks/.gitkeep` | tracked | `RESEARCH_ONLY` |
| `opencode.json` | tracked | `LOCAL_ONLY` |
| `pytest.ini` | tracked | `SANITIZE_AND_PUBLISH` |
| `requirements-dev.txt` | tracked | `SANITIZE_AND_PUBLISH` |
| `requirements.txt` | tracked | `SANITIZE_AND_PUBLISH` |
| `scripts/analyze_coordinate_framing_codec.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_correlation_results.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_d_x_join_residue.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_d_x_owned_period60.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_d_x_period60_followup.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_d_x_quotient_carry.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_d_y_independent_fields.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_d_y_serialization.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_designdocument_transformed.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_hc7_frames.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_join_codec_corpus.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_dependent_tables.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_header_sum.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_input_display_roles.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_model_uncertainty.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_r1_fields.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_r2_records.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_region5_packing.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_route_corpus.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_shadow_models.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_ui_after_x991.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_kalyaska_x999_tables.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_local_c_endpoint_corpus.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_local_c_x727_result.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_local_c_x728_result.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_local_c_x729_result.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_local_c_x_models.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_local_d_join_composition.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_local_d_xy_cross_capture.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_local_x_endpoint_capture.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_r0_r6.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_r4_frame_groups.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_region5_corpus.py` | tracked | `SANITIZE_AND_PUBLISH` |
| `scripts/analyze_region5_semantic.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_region5_semantic_correlation.py` | tracked | `RESEARCH_ONLY` |
| `scripts/analyze_trace_and_derive_rule.py` | tracked | `RESEARCH_ONLY` |
| `scripts/assess_live_import_uleb_candidates.py` | tracked | `RESEARCH_ONLY` |
| `scripts/build_kalyaska_x1000_research_candidate.py` | tracked | `RESEARCH_ONLY` |
| `scripts/build_kalyaska_x991_research_candidate.py` | tracked | `RESEARCH_ONLY` |
| `scripts/build_local_endpoint_emb.py` | tracked | `RESEARCH_ONLY` |
| `scripts/build_local_endpoint_serialization_map.py` | tracked | `RESEARCH_ONLY` |
| `scripts/build_local_positioned_emb.py` | tracked | `RESEARCH_ONLY` |
| `scripts/capture_designdocument_save.py` | tracked | `RESEARCH_ONLY` |
| `scripts/capture_saved_emt_read_key.py` | tracked | `RESEARCH_ONLY` |
| `scripts/check_dataset.py` | tracked | `RESEARCH_ONLY` |
| `scripts/checkpoint_kalyaska_x991.py` | tracked | `RESEARCH_ONLY` |
| `scripts/compare_d_y029_frozen_capture.py` | tracked | `RESEARCH_ONLY` |
| `scripts/compare_d_y030_frozen_capture.py` | tracked | `RESEARCH_ONLY` |
| `scripts/compare_d_y038_frozen_capture.py` | tracked | `RESEARCH_ONLY` |
| `scripts/compare_d_y_frozen_prediction.py` | tracked | `RESEARCH_ONLY` |
| `scripts/compare_existing_r2_prefixes.py` | tracked | `RESEARCH_ONLY` |
| `scripts/compare_region5_probe_c.py` | tracked | `RESEARCH_ONLY` |
| `scripts/compare_shift_design_document_properties.py` | tracked | `RESEARCH_ONLY` |
| `scripts/create_offline_translation_copy.py` | tracked | `RESEARCH_ONLY` |
| `scripts/disasm_live_import_function.py` | tracked | `RESEARCH_ONLY` |
| `scripts/dump_designdocument_stream.py` | tracked | `RESEARCH_ONLY` |
| `scripts/dump_live_import_function.py` | tracked | `RESEARCH_ONLY` |
| `scripts/dump_live_import_uleb_candidates.py` | tracked | `RESEARCH_ONLY` |
| `scripts/edit_kalyaska_bounded.py` | tracked | `RESEARCH_ONLY` |
| `scripts/encode_local_d_transformed.py` | tracked | `RESEARCH_ONLY` |
| `scripts/encode_local_d_x_transformed.py` | tracked | `RESEARCH_ONLY` |
| `scripts/encode_local_d_y_transformed.py` | tracked | `RESEARCH_ONLY` |
| `scripts/encode_local_positioned_transformed.py` | tracked | `RESEARCH_ONLY` |
| `scripts/find_kalyaska_live_header_refs.py` | tracked | `RESEARCH_ONLY` |
| `scripts/find_live_import_vtable_xrefs.py` | tracked | `RESEARCH_ONLY` |
| `scripts/find_visible_wilcom.py` | tracked | `RESEARCH_ONLY` |
| `scripts/freeze_kalyaska_x1000_post_transition.py` | tracked | `RESEARCH_ONLY` |
| `scripts/freeze_kalyaska_x981_width_probe.py` | tracked | `RESEARCH_ONLY` |
| `scripts/freeze_kalyaska_x991.py` | tracked | `RESEARCH_ONLY` |
| `scripts/freeze_kalyaska_x998.py` | tracked | `RESEARCH_ONLY` |
| `scripts/freeze_kalyaska_x9985_precision.py` | tracked | `RESEARCH_ONLY` |
| `scripts/freeze_kalyaska_x999.py` | tracked | `RESEARCH_ONLY` |
| `scripts/freeze_local_c_x727_prediction.py` | tracked | `RESEARCH_ONLY` |
| `scripts/freeze_local_c_x728_prediction.py` | tracked | `RESEARCH_ONLY` |
| `scripts/freeze_local_c_x729_prediction.py` | tracked | `RESEARCH_ONLY` |
| `scripts/generate_region5_from_source.py` | tracked | `RESEARCH_ONLY` |
| `scripts/generate_region5_native.py` | tracked | `RESEARCH_ONLY` |
| `scripts/inspect_emb.py` | tracked | `RESEARCH_ONLY` |
| `scripts/inspect_kalyaska_native_header_refs.py` | tracked | `RESEARCH_ONLY` |
| `scripts/inspect_kalyaska_route_boundaries.py` | tracked | `RESEARCH_ONLY` |
| `scripts/integrate_local_c_y3631_evidence.py` | tracked | `RESEARCH_ONLY` |
| `scripts/local_c_y_discriminator.py` | tracked | `RESEARCH_ONLY` |
| `scripts/orchestrate_region5_trace.py` | tracked | `RESEARCH_ONLY` |
| `scripts/parse_designdocument.py` | tracked | `RESEARCH_ONLY` |
| `scripts/popup_watcher.py` | tracked | `RESEARCH_ONLY` |
| `scripts/probe_candidate_serializers.py` | tracked | `RESEARCH_ONLY` |
| `scripts/probe_save_serializer_stalker.py` | tracked | `RESEARCH_ONLY` |
| `scripts/probe_save_variable_memcopies.py` | tracked | `RESEARCH_ONLY` |
| `scripts/probe_save_wrapper_caller.py` | tracked | `RESEARCH_ONLY` |
| `scripts/probe_single_save_destination.py` | tracked | `RESEARCH_ONLY` |
| `scripts/probe_virtual_serializer.py` | tracked | `RESEARCH_ONLY` |
| `scripts/probe_wilcom_compression_modules.py` | tracked | `RESEARCH_ONLY` |
| `scripts/re_3d4350.py` | tracked | `RESEARCH_ONLY` |
| `scripts/re_3d43f0.py` | tracked | `RESEARCH_ONLY` |
| `scripts/re_3d4400.py` | tracked | `RESEARCH_ONLY` |
| `scripts/re_5b60e0.py` | tracked | `RESEARCH_ONLY` |
| `scripts/re_5b60e0_broad.py` | tracked | `RESEARCH_ONLY` |
| `scripts/re_coml2_c2f0.py` | tracked | `RESEARCH_ONLY` |
| `scripts/re_coml2_origin.py` | tracked | `RESEARCH_ONLY` |
| `scripts/reconstruct_kalyaska_structure.py` | tracked | `RESEARCH_ONLY` |
| `scripts/resume_kalyaska_shadow_selection.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_designdocument_aab.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_kalyaska_shadow.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_local_c_x727_probe.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_local_c_x728_probe.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_local_c_x729_probe.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_local_d_x_probe.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_local_d_xy_cross_probe.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_local_positioned_tasks.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_local_post_edit_noop.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_local_x_endpoint_capture.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_probe_b_controlled_saveas.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_probe_b_with_saveas.py` | tracked | `RESEARCH_ONLY` |
| `scripts/run_probe_c_controlled_saveas.py` | tracked | `RESEARCH_ONLY` |
| `scripts/saveas_automation_v2.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_adversarial_discriminator.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_adversarial_v2.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_adversarial_v3.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_coordinate_regions_same_session.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_backing_buffer.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_coml2_file_source.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_coml2_physical_reads.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_coml2_stream_source.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_compressed_buffered_writer.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_compressed_writer.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_full_compressed_write.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_pre_rc4_source.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_r14_call_transitions.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_rc4_key_setup.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_rc4_transform.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_ctrl_n_underlying_reader.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_field1_before_open.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_field1_bytepack.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_field1_minimal.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_field1_open_then_saveas.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_field1_origin.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_field1_origin_simple.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_field1_with_saveas.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_3d4343_entry_diagnostic.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_3d4350_stalker.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_3d43f0_buffer_flow.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_3d43f0_stalker.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_3d447a_producer.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_665560.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_665560_caller.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_665560_pc1_stash.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_665560_source.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_import_665680.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_region5_container_construction.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_region5_materialization.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_region5_probe_a.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_region5_probe_b.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_region5_probe_c.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_region5_uleb_sequence.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trace_wilcom_emt_save_cipher.py` | tracked | `RESEARCH_ONLY` |
| `scripts/trigger_save_as_for_container_trace.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_guarded_c_y_codec.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_guarded_d_x_join_codec.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_guarded_d_y_join_codec.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_kalyaska_local_route_hypothesis.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_kalyaska_post_transition.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_kalyaska_shadow_evidence.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_kalyaska_source_reconstruction.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_kalyaska_structural_corpus.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_local_a_offline_encoder.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_local_b_x_offline_encoder.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_local_c_b_y_offline_encoder.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_local_c_x_offline_encoder.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_local_d_x_offline_encoder.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_local_d_y_offline_encoder.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_local_endpoint_emb_in_wilcom.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_modified_emt_in_wilcom.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_offline_coordinate_translation.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_offline_translation_in_wilcom.py` | tracked | `RESEARCH_ONLY` |
| `scripts/validate_position_core_captures.py` | tracked | `RESEARCH_ONLY` |
| `scripts/verify_normal_emt_archive_chain.py` | tracked | `RESEARCH_ONLY` |
| `scripts/wilcom_shadow_gui.py` | tracked | `RESEARCH_ONLY` |
| `src/__init__.py` | tracked | `RESEARCH_ONLY` |
| `src/build_dataset.py` | tracked | `RESEARCH_ONLY` |
| `src/contents_parser.py` | tracked | `RESEARCH_ONLY` |
| `src/ddd_parser.py` | tracked | `RESEARCH_ONLY` |
| `src/design_document_c_y_codec.py` | tracked | `RESEARCH_ONLY` |
| `src/design_document_d_y_codec.py` | tracked | `RESEARCH_ONLY` |
| `src/design_document_join_codec.py` | tracked | `RESEARCH_ONLY` |
| `src/design_document_local_mutation.py` | tracked | `RESEARCH_ONLY` |
| `src/design_document_position_core.py` | tracked | `RESEARCH_ONLY` |
| `src/design_document_properties.py` | tracked | `RESEARCH_ONLY` |
| `src/design_document_translation.py` | tracked | `RESEARCH_ONLY` |
| `src/dst_parser.py` | tracked | `SANITIZE_AND_PUBLISH` |
| `src/emb_reader.py` | tracked | `RESEARCH_ONLY` |
| `src/emt_design_document.py` | tracked | `RESEARCH_ONLY` |
| `src/export_stricts_pairs.py` | tracked | `RESEARCH_ONLY` |
| `src/generated_dataset.py` | tracked | `RESEARCH_ONLY` |
| `src/kalyaska_bounded_editor.py` | tracked | `RESEARCH_ONLY` |
| `src/kalyaska_local_route_hypothesis.py` | tracked | `RESEARCH_ONLY` |
| `src/kalyaska_post_transition_hypothesis.py` | tracked | `RESEARCH_ONLY` |
| `src/kalyaska_shadow_research.py` | tracked | `RESEARCH_ONLY` |
| `src/kalyaska_structural_diagnostics.py` | tracked | `RESEARCH_ONLY` |
| `src/local_positioned_authority.py` | tracked | `RESEARCH_ONLY` |
| `src/local_positioned_task_runner.py` | tracked | `RESEARCH_ONLY` |
| `src/local_positioned_tasks.py` | tracked | `RESEARCH_ONLY` |
| `src/wilcom_shadow_runner.py` | tracked | `RESEARCH_ONLY` |
| `tests/analyze_dst.py` | tracked | `RESEARCH_ONLY` |
| `tests/analyze_dst_commands.py` | tracked | `RESEARCH_ONLY` |
| `tests/analyze_duplicate_contents_diffs.py` | tracked | `RESEARCH_ONLY` |
| `tests/analyze_edr.py` | tracked | `RESEARCH_ONLY` |
| `tests/analyze_position_duplicate_groups.py` | tracked | `RESEARCH_ONLY` |
| `tests/automate_wilcom_batch.py` | tracked | `RESEARCH_ONLY` |
| `tests/automate_wilcom_file.py` | tracked | `RESEARCH_ONLY` |
| `tests/automate_wilcom_grouped_batch.py` | tracked | `RESEARCH_ONLY` |
| `tests/automate_wilcom_grouped_file.py` | tracked | `RESEARCH_ONLY` |
| `tests/compare_records.py` | tracked | `RESEARCH_ONLY` |
| `tests/compare_rose_emb_dst.py` | tracked | `RESEARCH_ONLY` |
| `tests/compare_shift_contents.py` | tracked | `RESEARCH_ONLY` |
| `tests/compare_shift_ddd.py` | tracked | `RESEARCH_ONLY` |
| `tests/compare_shift_design_icon.py` | tracked | `RESEARCH_ONLY` |
| `tests/compare_shift_dst.py` | tracked | `RESEARCH_ONLY` |
| `tests/compare_shift_emb.py` | tracked | `RESEARCH_ONLY` |
| `tests/compare_streams.py` | tracked | `RESEARCH_ONLY` |
| `tests/conftest.py` | tracked | `RESEARCH_ONLY` |
| `tests/dump_contents_region.py` | tracked | `RESEARCH_ONLY` |
| `tests/find_emb_reference_files.py` | tracked | `RESEARCH_ONLY` |
| `tests/generate_coordinate_variants.py` | tracked | `RESEARCH_ONLY` |
| `tests/inspect_wilcom_save_as.py` | tracked | `RESEARCH_ONLY` |
| `tests/integration/test_corpus.py` | tracked | `RESEARCH_ONLY` |
| `tests/integration/test_kalyaska_bounded_editor_offline_integration.py` | tracked | `RESEARCH_ONLY` |
| `tests/integration/test_normal_emt_design_document.py` | tracked | `RESEARCH_ONLY` |
| `tests/integration/test_normal_emt_non_identity_round_trip.py` | tracked | `RESEARCH_ONLY` |
| `tests/integration/test_normal_emt_round_trip.py` | tracked | `RESEARCH_ONLY` |
| `tests/integration/test_strict_pairs_dataset.py` | tracked | `RESEARCH_ONLY` |
| `tests/mine_contents_properties.py` | tracked | `RESEARCH_ONLY` |
| `tests/plot dst.py` | tracked | `RESEARCH_ONLY` |
| `tests/probe_design_document.py` | tracked | `RESEARCH_ONLY` |
| `tests/rank_emb_dst_pairs.py` | tracked | `RESEARCH_ONLY` |
| `tests/scan_contents_position_field.py` | tracked | `RESEARCH_ONLY` |
| `tests/scan_contents_xy_fields.py` | tracked | `RESEARCH_ONLY` |
| `tests/scan_originals.py` | tracked | `RESEARCH_ONLY` |
| `tests/search_emb_numeric_fingerprints.py` | tracked | `RESEARCH_ONLY` |
| `tests/test_ddd_parser.py` | tracked | `RESEARCH_ONLY` |
| `tests/test_dst_parser.py` | tracked | `RESEARCH_ONLY` |
| `tests/test_parser.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_automate_wilcom_batch.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_automate_wilcom_file.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_automate_wilcom_grouped_batch.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_automate_wilcom_grouped_file.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_build_dataset_unit.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_capture_artifact_guards.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_compare_region5_probe_c.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_contents_parser_unit.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_ddd_parser_helpers.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_design_document_c_y_codec.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_design_document_d_y_codec.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_design_document_join_codec.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_design_document_local_mutation.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_design_document_position_core.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_design_document_properties.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_design_document_translation.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_dst_parser_unit.py` | tracked | `SANITIZE_AND_PUBLISH` |
| `tests/unit/test_emt_design_document.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_generate_coordinate_variants.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_generated_dataset.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_inspect_wilcom_save_as.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_kalyaska_bounded_editor.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_kalyaska_local_route_hypothesis.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_kalyaska_post_transition_hypothesis.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_kalyaska_research_models.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_kalyaska_shadow_research.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_kalyaska_shadow_resume.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_kalyaska_structural_diagnostics.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_local_c_endpoint_evidence.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_local_c_x727_evidence.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_local_c_x728_evidence.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_local_c_x729_evidence.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_local_c_x_candidate_analysis.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_local_positioned_authority.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_local_positioned_task_runner.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_local_positioned_tasks.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_rank_logic.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_run_local_positioned_tasks_cli.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_trace_region5_probe_c.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_verify_positioned_dataset.py` | tracked | `RESEARCH_ONLY` |
| `tests/unit/test_wilcom_shadow_ownership.py` | tracked | `RESEARCH_ONLY` |
| `tests/validate_contents_scalars.py` | tracked | `RESEARCH_ONLY` |
| `tests/verify_positioned_dataset.py` | tracked | `RESEARCH_ONLY` |
| `x_minus_1_diff.txt` | tracked | `RESEARCH_ONLY` |
| `.hermes.md` | untracked | `LOCAL_ONLY` |
| `CURRENT_PROJECT_STATE.md` | untracked | `LOCAL_ONLY` |
| `PROMPT_SAVEAS_STATIC_REVIEW.md` | untracked | `LOCAL_ONLY` |
| `docs/reverse_engineering/PF17_SOURCE_CLOSURE_20260924.md` | untracked | `SANITIZE_AND_PUBLISH` |
| `nul` | untracked | `LOCAL_ONLY` |
| `r5_e15_functiontag_callers.py` | untracked | `RESEARCH_ONLY` |
| `r5_e15_functiontag_chain.py` | untracked | `RESEARCH_ONLY` |
| `review_findings.json` | untracked | `LOCAL_ONLY` |
| `review_findings_current.json` | untracked | `LOCAL_ONLY` |
| `scripts/__init__.py` | untracked | `RESEARCH_ONLY` |
| `scripts/analyze_macro_pf_static.py` | untracked | `RESEARCH_ONLY` |
| `scripts/capture_macro_pf_causality.py` | untracked | `RESEARCH_ONLY` |
| `scripts/capture_macro_pf_heap_links.py` | untracked | `RESEARCH_ONLY` |
| `scripts/probe_c_spec.py` | untracked | `RESEARCH_ONLY` |
| `scripts/run_probe_c_controlled_saveas_v2.py` | untracked | `RESEARCH_ONLY` |
| `scripts/run_probe_c_saveas_filename_preflight.py` | untracked | `RESEARCH_ONLY` |
| `scripts/run_wilcom_open_delivery_diagnostic.py` | untracked | `RESEARCH_ONLY` |
| `tests/unit/test_analyze_macro_pf_static.py` | untracked | `RESEARCH_ONLY` |
| `tests/unit/test_probe_c_v2_orchestration.py` | untracked | `RESEARCH_ONLY` |
| `tests/unit/test_region5_physical_codec.py` | untracked | `SANITIZE_AND_PUBLISH` |
| `tests/unit/test_region5_retrospective_controls.py` | untracked | `RESEARCH_ONLY` |
| `tests/unit/test_wilcom_open_delivery_diagnostic.py` | untracked | `RESEARCH_ONLY` |

## Published derivations

| Source material | Public result |
|---|---|
| Region5 codec functions in the corpus analyzer and their focused tests | `src/embroideryai/region5.py`, `tests/test_region5.py` |
| e4.2 StateStore insertion/storage findings and separately scoped e1.5 writer traversal | `src/embroideryai/state_store.py`, `docs/region5/ordering.md` |
| PF17 source-closure report | `docs/reverse_engineering/pf17-source-rule.md` |
| DST parser and deterministic tests | `src/embroideryai/dst.py`, `tests/test_dst.py` |
| Evidence-discipline rules and checkpoint language | `src/embroideryai/evidence.py`, methodology/status documentation |

## Explicit exclusions

The snapshot intentionally excludes runtime orchestration, live instrumentation, raw evidence, captured memory, executable images, proprietary libraries, private hashes, absolute paths, customer-like designs, target-derived retrospective generators, local prompts, review logs, nested repositories, and generated caches.

## Final license selection

The project owner explicitly selected the MIT License for the public snapshot. The standard license text is included in `LICENSE` with copyright year 2026 and holder Rudolf.
