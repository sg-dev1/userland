{
    'includes': {
      '../../../../config.gypi',
    },
    'targets': [
      {
        'target_name': 'mmal_util_static',
        'type': 'static_library',
        'dependencies': [
          '<(DEPTH)/userland/interface/vcos/pthreads/vcos_pthreads.gyp:vcos_pthreads_static',
        ],
        #'defines': [
        #  'DEFINE_FOO',
        #  'DEFINE_A_VALUE=value',
        #],
        'include_dirs': [
          '..',
        ],
        'sources': [
          'mmal_il.c',
          'mmal_util.c',
          'mmal_connection.c',
          'mmal_graph.c',
          'mmal_list.c',
          'mmal_param_convert.c',
          'mmal_util_params.c',
          'mmal_component_wrapper.c',
          'mmal_util_rational.c',
        ],
      },
    ],
}
