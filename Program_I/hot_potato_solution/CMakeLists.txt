cmake_minimum_required(VERSION 3.0.0)
project(HP_Solution VERSION 0.1.0)

add_executable(HP_Solution hot_potato_solution.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
