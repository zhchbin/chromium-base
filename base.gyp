{
  'targets': [
    {
      'target_name': 'base',
      'type': 'static_library',
      'direct_dependent_settings': {
        'include_dirs': [
          'src',
        ],
      },
      'include_dirs': [
        'src',
      ],
      'sources': [
        'src/base/base_export.h',
        'src/base/basictypes.h',
        'src/base/compiler_specific.h',
        'src/base/memory/ref_counted.h',
        'src/base/memory/scoped_handle.h',
        'src/base/memory/scoped_policy.h',
        'src/base/memory/scoped_ptr.h',
        'src/base/memory/scoped_vector.h',
        'src/base/memory/weak_ptr.cc',
        'src/base/memory/weak_ptr.h',
        'src/base/move.h',
        'src/base/stl_util.h',
        'src/base/template_util.h',
        'src/build/build_config.h',
      ],
    },
  ],
}
