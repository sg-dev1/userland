{
    'includes': {
      '../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'dummy_writer_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/containers/containers.gyp:containers_static',
        ],
        'include_dirs': [
          '<(DEPTH)/userland',
        ],
        'sources': [
          'dummy_writer.c',
        ],
      },
    ],
}
