#include "hello/hello_node.hpp"

int main(int argc,char * argv[]){
    rclcpp::init(argc,argv);

    auto node = std::make_shared<HelloNode>();

    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}