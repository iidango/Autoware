#ifndef VEHICLE_MONITOR_PAINTER_HPP
#define VEHICLE_MONITOR_PAINTER_HPP

#include <QPainter>

namespace autoware_rviz_plugins {

class VehicleMonitorPainter : public QPainter
{
    public:

        VehicleMonitorPainter(QPaintDevice* device);

        void drawPieChart(int x, int y, int r, int ang, int anglen, const QColor &color);
};

}

#endif
