import React, {Component} from "react";
import axios from "axios";
import { API_URL } from "../api_access";


class UserList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            users: [],
        };
    }

    componentDidMount() {
        axios.get(`${API_URL}/usuarios`).then((response) => {
            this.setState({ users: response.users });
        });
    }

    render() {
        const { users } = this.state;
        return (
            <div>
                <table>
                    <thead>
                        <th>Nome</th>
                        <th>Raça</th>
                        <th>Cor</th>
                    </thead>
                    <tbody>
                        {users.map((user) => (
                            <tr key={user.id}>
                                <td>{user.nome}</td>
                                <td>{user.raça}</td>
                                <td>{user.cor}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    }
}

export default UserList;