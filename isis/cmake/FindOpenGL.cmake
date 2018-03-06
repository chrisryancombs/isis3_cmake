# CMake module for find_package(OpenGL)
# Finds include directory and all applicable libraries
#
# Sets the following:
#   KAKADU_INCLUDE_DIR
#   KAKADU_A_LIBRARY
#   KAKADU_V_LIBRARY

find_path(OPENGL_INCLUDE_DIR
  NAME gl.h
)

find_library(GL_LIBRARY
  NAMES GL
)

find_library(GLU_LIBRARY
  NAMES GLU
)

get_filename_component(OPENGL_INCLUDE_DIR "${OPENGL_INCLUDE_DIR}" DIRECTORY)
