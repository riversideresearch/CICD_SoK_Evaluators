cmake_minimum_required(VERSION 3.14)
project(unpinned_eval)

include(FetchContent)

FetchContent_Declare(
    lib_unpinned
    GIT_REPOSITORY https://github.com/riversideresearch/CICD_SoK_Evaluators.git
    GIT_TAG main
)

FetchContent_MakeAvailable(lib_unpinned)

add_executable(unpinned_eval main.c)
target_link_libraries(unpinned_eval PRIVATE lib_unpinned)
