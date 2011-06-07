#ifndef ResidualMagnitudeFilter_H
#define ResidualMagnitudeFilter_H

#include "AbstractNumberFilter.h"


class QString;


namespace Isis
{
  class AbstractFilterSelector;
  class ControlCubeGraphNode;
  class ControlMeasure;
  class ControlPoint;
  
  class ResidualMagnitudeFilter : public AbstractNumberFilter
  {
      Q_OBJECT

    public:
      ResidualMagnitudeFilter(AbstractFilter::FilterEffectivenessFlag flag,
          AbstractFilterSelector *, int minimumForSuccess = -1);
      virtual ~ResidualMagnitudeFilter();
      bool evaluate(const ControlCubeGraphNode *) const;
      bool evaluate(const ControlPoint *) const;
      bool evaluate(const ControlMeasure *) const;
      QString getImageDescription() const;
      QString getPointDescription() const;
      QString getMeasureDescription() const;
  };
}

#endif