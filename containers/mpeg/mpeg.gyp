{
    'includes': {
      '../../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'ps_reader_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/containers/containers.gyp:containers_static',
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
          '<(DEPTH)/userland',
        ],
        'sources': [
          'ps_reader.c',
        ],
      },
    ],
}
