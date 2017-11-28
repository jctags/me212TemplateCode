#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/src/me212pillbed"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/install/lib/python2.7/dist-packages:/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/build" \
    "/usr/bin/python" \
    "/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/src/me212pillbed/setup.py" \
    build --build-base "/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/build/me212pillbed" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/install" --install-scripts="/home/robot/Desktop/me212s3/MobileRobot/catkin_ws/install/bin"
