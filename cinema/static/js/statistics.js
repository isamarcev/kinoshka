// FILM PIE

anychart.onDocumentReady(function () {
      // The data used in this sample can be obtained from the CDN
      // https://cdn.anychart.com/samples/maps-bubble/bubble-christian-map/data.json
      anychart.data.loadJsonFile(
        'https://cdn.anychart.com/samples/maps-bubble/bubble-christian-map/data.json',
        function (data) {
          var dataSet = anychart.data.set(data);
          var mapping = dataSet.mapAs({
            name: 'name',
            id: 'id',
            size: 'amount',
            value: 'percent'
          });

          // Creates Map Chart
          var map = anychart.map();
          map.padding([20, 0, 10, 0]);
          // Sets geodata using https://cdn.anychart.com/geodata/latest/custom/world/world.js
          map.geoData('anychart.maps.world');

          map
            .credits()
            .enabled(true)
            .url('https://en.wikipedia.org/wiki/Christianity_by_country')
            .text(
              'Data source: https://en.wikipedia.org/wiki/Christianity_by_country'
            )
            .logoSrc('https://en.wikipedia.org/static/favicon/wikipedia.ico');

          // Sets Chart Title
          map
            .title()
            .enabled(true)
            .text('Посетители')
            .padding([0, 0, 10, 0]);

          // Sets bubble max size settings
          map.minBubbleSize('0.5%').maxBubbleSize('5%');

          // Creates bubble series1
          var series1 = map.bubble(mapping);
          // Sets series1 settings
          series1
            .name('Мужчины')
            // Sets series1 geo id field settings
            .geoIdField('iso_a2')
            .fill('#1976d2 0.6')
            .stroke('1 #1976d2 0.9');
          series1
            .legendItem()
            .iconType('circle')
            .iconFill('#1976d2 0.6')
            .iconStroke('1 #1976d2 0.9');

          var series2 = map.choropleth(mapping);
          series2
            .name('Женщины')
            .geoIdField('iso_a2')
            .legendItem({ iconFill: '#b0bec5' });
          series2.hovered().fill(series2.fill());
          series2.colorScale(
            anychart.scales.linearColor('#f7f7f7', '#b0bec5')
          );

          map
            .legend()
            .enabled(true)
            .position('center-top')
            .align('center')
            .itemsLayout('horizontal')
            .padding(0, 0, 30, 0)
            .paginator(false);
          map.interactivity().selectionMode('none');

          map
            .tooltip()
            .useHtml(true)
            .title({ fontColor: '#7c868e' })
            .padding([8, 13, 10, 13])
            .format(function () {
              var value =
                '<span style="color: #545f69; font-size: 12px; font-weight: bold">';
              var description =
                '<br/><span style="color: #7c868e; font-size: 12px; font-style: italic">';
              return (
                value +
                parseInt(this.getData('amount')).toLocaleString('en-US') +
                '</span></strong>' +
                description +
                this.getData('percent') +
                '%</span>'
              );
            });

          map
            .tooltip()
            .background()
            .enabled(true)
            .fill('#fff')
            .stroke('#c1c1c1')
            .corners(3)
            .cornerType('round');

          // create zoom controls
          var zoomController = anychart.ui.zoom();
          zoomController.render(map);

          // Sets container id for the chart
          map.container('container');
          // Initiates chart drawing
          map.draw();
        }
      );
    });

