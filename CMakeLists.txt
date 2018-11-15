cmake_minimum_required(VERSION 3.5.0)
set(CMAKE_VERBOSE_MAKEFILE ON)

project(collisions)

#Boost and its components
find_package (Boost REQUIRED)

if (NOT Boost_FOUND)
	message(STATUS "This project requires the Boost library, and will not be compiled.")
	return()
endif()

# CGAL and its components
find_package(CGAL QUIET COMPONENTS Core GMP MPFI)

if (NOT CGAL_FOUND)
  message(STATUS "This project requires the CGAL library, and will not be compiled.")
  return()
endif()

# include helper file
include( ${CGAL_USE_FILE})


set (SOURCE_DIR "collisions/cpp")
include_directories (${SOURCE_DIR})

add_subdirectory(pybind11)
pybind11_add_module(c_collisions ${SOURCES} "${SOURCE_DIR}/c_collisions.cpp" )
