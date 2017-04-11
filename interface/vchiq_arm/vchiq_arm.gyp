{
    'includes': {
      '../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'vchiq_arm_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/interface/mmal/core/mmal_core.gyp:mmal_core_static',
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        #'include_dirs': [
        #  '<(DEPTH)/userland/interface/mmal',
        #],
        'sources': [
          'vchiq_lib.c',
          'vchiq_util.c',
        ],
      },
    ],
}
