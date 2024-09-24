uname_result=$(uname -a | awk '{print tolower($0)}')
case ${uname_result} in
    *openwrt*)
        echo "Installing in OpenWRT..."
        install -m 755 ./platform/OpenWRT/NJUPTNetwork /etc/init.d/NJUPTnetwork
        /etc/init.d/NJUPTnetwork enable
        /etc/init.d/NJUPTnetwork start
        ;;
    *)
        echo "Error: Unsupported platform!"
        ;;
esac
