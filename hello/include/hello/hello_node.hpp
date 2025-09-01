#include <rclcpp/rclcpp.hpp>
#include <rclcpp/qos.hpp>

class HelloNode : public rclcpp::Node
{
private:
    rclcpp::TimerBase::SharedPtr timer_;

    void timer_callback();

public:
    HelloNode(const rclcpp::NodeOptions &options = rclcpp::NodeOptions());
    HelloNode(const std::string& name_space, const rclcpp::NodeOptions& options = rclcpp::NodeOptions());
    
};