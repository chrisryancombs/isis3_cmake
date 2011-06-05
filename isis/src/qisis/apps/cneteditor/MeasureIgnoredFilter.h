#ifndef MeasureIgnoredFilter_H
#define MeasureIgnoredFilter_H

#include "AbstractFilter.h"


namespace Isis
{
  class AbstractFilterSelector;
  class ControlCubeGraphNode;
  class ControlMeasure;
  
  class MeasureIgnoredFilter : public AbstractFilter
  {
      Q_OBJECT

    public:
      MeasureIgnoredFilter(AbstractFilter::FilterEffectivenessFlag flag,
          AbstractFilterSelector *, int minimumForImageSuccess = -1);
      virtual ~MeasureIgnoredFilter();
      bool evaluate(const ControlCubeGraphNode *) const;
      bool evaluate(const ControlPoint *) const;
      bool evaluate(const ControlMeasure *) const;
      QString getImageDescription() const;
      QString getPointDescription() const;
      QString getMeasureDescription() const;
  };
}

#endif