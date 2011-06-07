#ifndef SampleResidualFilter_H
#define SampleResidualFilter_H

#include "AbstractNumberFilter.h"


class QString;


namespace Isis
{
  class AbstractFilterSelector;
  class ControlCubeGraphNode;
  class ControlMeasure;
  class ControlPoint;
  
  class SampleResidualFilter : public AbstractNumberFilter
  {
      Q_OBJECT

    public:
      SampleResidualFilter(AbstractFilter::FilterEffectivenessFlag flag,
          AbstractFilterSelector *, int minimumForSuccess = -1);
      virtual ~SampleResidualFilter();
      bool evaluate(const ControlCubeGraphNode *) const;
      bool evaluate(const ControlPoint *) const;
      bool evaluate(const ControlMeasure *) const;
      QString getImageDescription() const;
      QString getPointDescription() const;
      QString getMeasureDescription() const;
  };
}

#endif