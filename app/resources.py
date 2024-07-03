from flask_restful import Resource, reqparse

from .models import BarModel


class BarResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='Необходимо ввести название бара'
    )
    parser.add_argument('inst_url', type=str, required=False)
    parser.add_argument('vk_url', type=str, required=False)
    parser.add_argument('tg_url', type=str, required=False)
    def get(self, id):
        bar = BarModel.find_bar_by_id(id)
        if bar:
            return {
                'id': bar.id,
                'name': bar.name,
                'inst_url': bar.inst_url,
                'vk_url': bar.vk_url,
                'tg_url': bar.tg_url
            }, 200
        else:
            return {'message': 'Бар не найден'}, 404

    def post(self):
        request_data = BarResource.parser.parse_args()
        new_bar = BarModel(name=request_data['name'],
                           vk_url=request_data['vk_url'],
                           inst_url=request_data['inst_url'],
                           tg_url=request_data['tg_url'])

        try:
            new_bar.save_to_db()
        except:
            return {'message': 'Не удалось записать бар в базу'}, 500

        return {
            'id': new_bar.id,
            'name': new_bar.name,
            'inst_url': new_bar.inst_url,
            'vk_url': new_bar.vk_url,
            'tg_url': new_bar.tg_url
        }

    def delete(self, id):
        bar = BarModel.find_bar_by_id(id)
        if bar:
            try:
                bar.delete_from_db()
                return {'message': f'Бар с id {id} удален из базы'}, 200
            except:
                return {'message': f'Не удалось удалить бар из базы'}, 500
        return {'message': 'Бар не найден'}


class BarsResource(Resource):
    def get(self):
        bars = BarModel.query.all()
        bars_json = {
            'bars': [
                {
                    'id': bar.id,
                    'name': bar.name,
                    'inst_url': bar.inst_url,
                    'vk_url': bar.vk_url,
                    'tg_url': bar.tg_url
                } for bar in bars
            ]
        }
        return bars_json