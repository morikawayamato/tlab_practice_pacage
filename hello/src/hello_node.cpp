#include "hello/hello_node.hpp"

HelloNode::HelloNode(const rclcpp::NodeOptions &options) : HelloNode("", options) {}
HelloNode::HelloNode(const std::string &name_space, const rclcpp::NodeOptions &options)
    : Node("hello_node", name_space, options)
{
    using namespace std::chrono_literals;

    timer_ = create_wall_timer(100ms,std::bind(&HelloNode::timer_callback,this));
}

void HelloNode::timer_callback(){
    RCLCPP_INFO(this->get_logger(),"Hello_World");
}